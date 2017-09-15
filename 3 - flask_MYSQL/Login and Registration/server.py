from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
import md5
app = Flask(__name__)
app.secret_key = 'key'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app,'logindb')

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
        session['user_id'] = user[0]['id']
        return redirect('/success')
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
        info = mysql.query_db(query, data)
        return render_template('r_success.html')
    else:
        return redirect('/')

@app.route('/success')
def success():
    return render_template('l_success.html')
app.run(debug=True)
