from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    welcome_message="Welcome to Flask page!"
    return render_template("welcome.html", welcome_message=welcome_message)


