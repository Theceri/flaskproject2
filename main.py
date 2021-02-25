from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def render_child():
    return render_template('child.html')