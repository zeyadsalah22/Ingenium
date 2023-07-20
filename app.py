import os
from cs50 import SQL
import werkzeug
from flask import Flask, flash, redirect, render_template, request, session
# Configure application
app = Flask(__name__)
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/drama")
def drama():
    return render_template("drama.html")

@app.route("/music")
def music():
    return render_template("music.html")

@app.route("/art")
def art():
    return render_template("art.html")

@app.route("/photography")
def photography():
    return render_template("photography.html")

@app.route("/design")
def design():
    return render_template("design.html")

@app.route("/media")
def media():
    return render_template("media.html")

@app.route("/logistics")
def logistics():
    return render_template("logistics.html")

@app.route("/hr")
def hr():
    return render_template("hr.html")

@app.route("/pr")
def pr():
    return render_template("pr.html")

@app.route("/literature")
def literature():
    return render_template("literature.html")

@app.route("/what")
def what():
    return render_template("what.html")

@app.route("/artsmania")
def artsmania():
    return render_template("artsmania.html")

@app.route("/high")
def high():
    return render_template("high.html")

@app.route("/application")
def application():
    return render_template("application.html")