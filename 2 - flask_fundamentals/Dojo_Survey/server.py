from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')
@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    city = request.form['city']
    lang = request.form['lang']
    comment = request.form['comment']
    print 'Name: ' + name
    print 'Dojo Location: ' + city
    print 'Favorite Language: ' + lang
    print 'Comment: ' + comment
    return render_template('result.html', n_name=name, c_city=city, l_lang=lang, c_comment=comment)
app.run(debug=True)
