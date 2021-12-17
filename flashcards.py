from flask import Flask, render_template
from model import db
app = Flask(__name__)

welcome_message="Welcome to Flask page!"

@app.route('/')
def hello_world():
    global welcome_message
    return render_template("welcome.html", welcome_message=welcome_message)


@app.route('/card')
def show_card():
    card = db[0]
    return render_template("card.html", card=card)