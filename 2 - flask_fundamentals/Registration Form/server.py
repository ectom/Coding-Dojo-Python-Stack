from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process', methods=['POST'])
def process():
    boolean = True
    length = True
    email = request.form['email']
    first = request.form['first']
    last = request.form['last']
    password = request.form['pass']
    confirm = request.form['confirm']
    if len(email) < 1 or len(first) < 1 or len(last) < 1 or len(password) < 1 or len(confirm) < 1: #check for blank fields
        flash('Do not leave any of the fields blank')
        boolean = False
        length = False
    if length == True:
        if not EMAIL_REGEX.match(email): #checks for valid email
            flash("Invalid Email Address!")
            boolean = False
        if first.isalpha() == False or last.isalpha() == False: #checks for numbers in name fields
            flash('Name cannot contain numbers')
            boolean = False
        if password != confirm: #checks if passwords are the same
            flash('Passwords do not match')
            boolean = False
        if len(password) < 8: #checks if password is at least 8 characters
            flash('Password must be at least 8 characters')
            boolean = False
    if boolean == True:
        return redirect('/submit')
    else:
        return redirect('/')
@app.route('/submit')
def submit():
    return render_template('submit.html')

app.run(debug=True)
