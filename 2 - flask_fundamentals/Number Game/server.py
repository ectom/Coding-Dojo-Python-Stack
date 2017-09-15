from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = 'key'


@app.route('/')
def index():
    session['keys'] = random.randrange(1,101)
    return render_template('index.html')
@app.route('/guess', methods=['POST'])
def guess():
    session['num'] = int(request.form['num'])
    if session['num'] == session['keys']:
        return render_template('win.html')
    elif session['num'] >= session['keys']:
        return render_template('high.html')
    elif session['num'] <= session['keys']:
        return render_template('low.html')
    return redirect('/')
app.run(debug=True)
