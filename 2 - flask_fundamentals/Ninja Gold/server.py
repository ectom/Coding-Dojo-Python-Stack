from flask import Flask, render_template, request, redirect, session
import random
import time
import datetime
app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def index():
    session['gold'] = 0
    session['activities'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    if request.form['building'] == 'farm':
        earned = random.randrange(10, 21)
        session['gold'] += earned
        session['activities'].append('Earned ' + str(earned) + ' gold from the farm! ' + str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')))
    elif request.form['building'] == 'cave':
        earned = random.randrange(5,11)
        session['gold'] += earned
        session['activities'].append('Earned ' + str(earned) + ' gold from the cave! ' + str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')))
    elif request.form['building'] == 'house':
        earned = random.randrange(2,6)
        session['gold'] += earned
        session['activities'].append('Earned ' + str(earned) + ' gold from the farm! ' + str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')))
    elif request.form['building'] == 'casino':
        earned = random.randrange(-50, 51)
        session['gold'] += earned
        if earned > 0:
            session['activities'].append('Entered a casino and won ' + str(earned) + ' gold! ' + str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')))
        if earned < 0:
            session['activities'].append('Entered a casino and lost ' + str(earned) + ' gold... ' + str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')))
        if earned == 0:
            session['activities'].append('Entered a casino and did not win or lose anything ' + str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')))

    return render_template('index.html', r=session['activities'])

app.run(debug=True)
