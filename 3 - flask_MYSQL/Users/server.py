from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = 'key'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app,'usersdb')

@app.route('/users', methods=['GET'])
def index():
    query = "SELECT id, first_name, last_name, email, DATE_FORMAT(created_at, '%M %D %Y') as created_at, DATE_FORMAT(updated_at, '%M %D %Y') as updated_at FROM users"
    all_users = mysql.query_db(query)
    return render_template('index.html', users = all_users)

@app.route('/users/new', methods=['GET'])
def new():
    return render_template('new.html')

@app.route('/users/create', methods=['POST'])
def create():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    query = 'INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())'
    mysql.query_db(query, data)
    return redirect('/users')

@app.route('/users/<a_id>', methods=['GET'])
def show(a_id):
    data = {'the_id': a_id}
    query = "SELECT id, first_name, last_name, email, created_at, updated_at FROM users WHERE users.id = :the_id"
    user = mysql.query_db(query, data)
    return render_template('show.html', users=user)

@app.route('/users/<user_id>/edit', methods=['GET'])
def edit(user_id):
    data = {'the_id': user_id}
    query = "SELECT id, first_name, last_name, email, created_at, updated_at FROM users WHERE users.id = :the_id"
    user = mysql.query_db(query, data)
    return render_template('edit.html', users = user)

@app.route('/editing', methods=['POST'])
def editing():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'the_id': request.form['hidden']
    }
    query = 'UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = NOW() WHERE users.id = :the_id'
    mysql.query_db(query, data)
    return redirect('/users')

@app.route('/users/<a_id>/destroy', methods=['GET'])
def destroy(a_id):
    data = {'the_id': a_id}
    query = 'DELETE FROM users WHERE users.id = :the_id'
    mysql.query_db(query, data)
    return redirect('/users')

app.run(debug = True)
