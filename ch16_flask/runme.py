# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:40:09 2019

@author: winkl
"""


from flask import Flask, render_template, request

heading = "<h1>Hello World!</h1>"
first_para = "<p>This is a paragraph, changed, update</p>"

app = Flask("MyApp")
@app.route("/index")
def header():
    everything = heading + first_para
    return everything

@app.route("/about")
def runtest():
    return render_template("about.html")

@app.route("/name/<name>")
def hello_someone(name):
    return render_template("name.html", name=name.title())

@app.route("/animal/<animal>")
def fav_animal(animal):
    return render_template("animal.html", animal=animal)

@app.route("/confirm", methods=["POST"])
def confirm():
    form_data = request.form
    email = form_data["email"]
    result="All OK"
    return render_template("confirm.html", title="Form confirmation", **locals())

app.run(debug=True)
