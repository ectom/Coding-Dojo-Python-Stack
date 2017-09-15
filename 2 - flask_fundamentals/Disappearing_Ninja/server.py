from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')
@app.route('/ninja/<color>')
def colors(color):
    if color == 'blue' or color == 'red' or color == 'orange' or color == 'purple':
        return render_template(color + '.html')
    else:
        return render_template('notapril.html')
app.run(debug=True)
