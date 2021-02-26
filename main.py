from flask import Flask, render_template, abort, redirect, url_for
app = Flask(__name__)

@app.route('/')
def redirect_login():
    # return render_template('child.html')
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fname = request.form['first_name']
        lname = request.form['last_name']
        print(fname, lname)