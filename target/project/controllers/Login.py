# -*- coding: utf-8 -*-
from project import app
from project.models.Dashboard import *
from flask import render_template, request, render_template_string, make_response, redirect, session
import uuid

@app.route("/login", methods=['GET', 'POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    session['username'] = username
    session['password'] = password
    if(password == "test" and username == "test"):
        random = uuid.uuid1()
        response = make_response(redirect('/confidential'))
        session['loggedin'] = random
        return response
    if request.method == 'POST':
        if(password == "admin" or username != "admin"):
            return render_template("login/index.html", error = "invalid username")
        if(password != "admin" or username == "admin"):
            return render_template("login/index.html", error = "invalid password for username")
    else:
        return render_template("login/index.html", error = "")


@app.route("/login/endsession", methods=['GET', 'POST'])
def logout():
    if not session.get('loggedin'):
        error = None
        return redirect("/dashboard/1", code=302)
    else:
        session.clear()
        return redirect("/dashboard/1", code=302)
