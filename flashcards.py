from flask import Flask, render_template, abort, request, redirect, url_for
from model import db, save_db

app = Flask(__name__)

welcome_message = "Welcome to Flask page!"


@app.route('/')
def welcome():
    return render_template("welcome.html", cards=db)


@app.route('/card/<int:index>')
def show_card(index):
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index, max_index=len(db) - 1)
    except IndexError:
        abort(404)


@app.route('/add_card', methods=["GET", "POST"])
def add_card():
    if request.method == "POST":
        card = {"question": request.form['question'],
                "answer": request.form['answer']}
        db.append(card)
        save_db()
        return redirect(url_for('show_card', index=len(db)-1))
    else:
        return render_template('add_card.html')


@app.route('/remove_card/<int:index>', methods=["GET", "POST"])
def remove_card(index):
    if request.method == "GET":
        card = db[index]
        return render_template("remove_card.html", card=card, index=index)
    elif request.method == "POST":
        del db[index]
        save_db()
        return redirect(url_for('welcome'))


