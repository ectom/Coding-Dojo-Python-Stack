from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
import md5
app = Flask(__name__)
app.secret_key = 'key'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app,'walldb')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():

    login_query = 'SELECT id, first_name, last_name, email, password FROM users WHERE email = :user_email'
    data = {'user_email': request.form['email']}
    user = mysql.query_db(login_query, data)
    if len(user) == 0:
        flash('Invalid Email or Password')
        return redirect('/')
    confirm = md5.new(request.form['password']).hexdigest()
    if confirm == user[0]['password']:
        session['id'] = user[0]['id']
        session['first_name'] = user[0]['first_name']
        return redirect('/wall')
    else:
        flash('Invalid Email or Password')
        return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password'],
        'confirm': request.form['confirm']
    }
    sufficient = True
    if len(data['first_name']) < 1:
        flash('First Name required')
        sufficient = False
    elif len(data['first_name']) < 3 and len(data['first_name']) > 0:
        flash('First Name is too short')
        sufficient = False
    if len(data['last_name']) < 1:
        flash('Last Name required')
        sufficient = False
    elif len(data['last_name']) < 3 and len(data['last_name']) > 0:
        flash('Last Name is too short')
        sufficient = False
    if len(data['email']) < 1:
        flash('Email required')
        sufficient = False
    elif not EMAIL_REGEX.match(data['email']):
        flash("Email is not valid!")
        sufficient = False
    if len(data['password']) < 1:
        flash('Password required')
        sufficient = False
    if len(data['password']) > 0 and len(data['password']) < 8:
        flash('Password must be at least 8 characters')
        sufficient = False
    if data['password'] != data['confirm']:
        flash('Passwords do not match')
        sufficient = False
    else:
        data['password'] = md5.new(data['password']).hexdigest()
    if sufficient == True:
        query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())'
        mysql.query_db(query, data)
        return redirect('/r_success')
    else:
        return redirect('/')

@app.route('/r_success')
def r_success():
    return render_template('r_success.html')

@app.route('/wall')
def wall():
    query = "SELECT users.first_name, users.last_name, messages.message, DATE_FORMAT(messages.created_at, '%M %D %Y'), messages.id FROM messages JOIN users ON messages.user_id = users.id"
    all_messages = mysql.query_db(query)
    print all_messages
    for message in all_messages:
		message['comments'] = []
		query = "SELECT users.first_name, users.last_name, DATE_FORMAT(comments.created_at, '%M %D %Y') as created_at, comments.comment, comments.id FROM comments JOIN users ON comments.user_id = users.id WHERE comments.message_id = :m_id"
		data = {"m_id": message['id']}
		message['comments']=mysql.query_db(query,data)
    return render_template('wall.html', messages=all_messages)

@app.route('/logout', methods=['POST'])
def logout():
    return redirect('/')

@app.route('/home', methods=['POST'])
def home():
    return redirect('/')

@app.route('/post', methods=['POST'])
def post():
    data = {
        'new_post': request.form['message'],
        'id': session['id']
    }
    query = 'INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:id, :new_post, NOW(), NOW())'
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/comment/<message_id>', methods=['POST'])
def comment(message_id):
    query = 'INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) VALUES (:u_id, :m_id, :cmt, NOW(), NOW())'
    data = {
        'u_id': session['user_id'],
        'm_id': message_id,
        'cmt': request.form['comment']
    }
    mysql.query_db(query, data)
    return redirect('/wall')

app.run(debug=True)
