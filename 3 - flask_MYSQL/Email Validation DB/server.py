from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'key'
mysql = MySQLConnector(app,'emaildb')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def create():
    data = {'a_email': request.form['email']}
    email = data['a_email']
    if not EMAIL_REGEX.match(email):
        flash("Email is not valid!")
        return redirect('/')
    query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:a_email, NOW(), NOW())"
    mysql.query_db(query, data)
    return redirect('/success')

@app.route('/success')
def success():
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query)
    return render_template('success.html', all_emails=emails)

@app.route('/delete', methods=['POST'])
def delete():
    data = {"deleted": request.form['delete']}
    query = 'DELETE FROM emails WHERE email = :deleted'
    mysql.query_db(query, data)
    return redirect('/success')
app.run(debug=True)
