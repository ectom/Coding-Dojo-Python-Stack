from flask import Flask, render_template, redirect, request, flash
app = Flask(__name__)
app.secret_key = 'key'

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
    if len(name) < 1:
        flash('Cannot leave your name blank')
    if len(comment) < 1:
        flash('Cannot leave the comments blank')
    elif len(comment) > 120:
        flash('Comments are too long')
    if len(name) > 0 and len(comment) > 0 and len(comment) < 120:
        return render_template('result.html', n_name=name, c_city=city, l_lang=lang, c_comment=comment)
    else:
        return redirect('/')
app.run(debug=True)
