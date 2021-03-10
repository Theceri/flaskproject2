from flask import Flask, render_template, abort, redirect, url_for
from configs.base_config import *
import psycopg2


app = Flask(__name__)
app.config.from_object(Development)


# Connect to an existing database
conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='1234'")
# try:
#     pass
# except:
#     print("I am unable to connect to the database")

#Open a cursor to perform database operations
cur = conn.cursor()

#Execute a command: this creates a new table
cur.execute("CREATE TABLE users (fname varchar, lname varchar, email varchar);")

@app.route('/')
def redirect_login():
    # return render_template('child.html')
    return "Hello world"

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fname = request.form['first_name']
        lname = request.form['last_name']
        print(fname, lname)

@app.route('/user/<username>')
def profile(username):
     # show the user profile for that user
    return f"my name is {username}"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

if __name__ == '__main__':
    app.run()