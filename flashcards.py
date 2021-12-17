from flask import Flask, render_template, abort
from model import db
app = Flask(__name__)

welcome_message="Welcome to Flask page!"

@app.route('/')
def welcome():
    global welcome_message
    return render_template("welcome.html", welcome_message=welcome_message)


@app.route('/card/<int:index>')
def show_card(index):
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index, max_index=len(db)-1)
    except IndexError:
        abort(404)

