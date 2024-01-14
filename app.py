from flask import Flask, redirect, render_template, request

from contacts_model import Contact


app = Flask(__name__)


@app.route("/")
def index():
    """Redirect root to contacts"""
    return redirect("/contacts")


@app.route("/contacts")
def contacts():
    """Contacts list"""
    search = request.args.get("q")
    if search is not None:
        contacts_set = Contact.search(search)
    else:
        contacts_set = Contact.all()
    return render_template("index.html", contacts=contacts_set)


@app.route("/hello")
def hello():
    """Hello world health check"""
    return "Hello, World!"
