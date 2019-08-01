from project import app
from project.models.Dashboard import *
from flask import render_template, request, render_template_string, make_response, redirect, session
import uuid

@app.route("/confidential", methods=['GET', 'POST'])
def xhr_get_info_stealing():
    if not session.get('loggedin'):
        return redirect("/dashboard/1", code=302)
    else:
        response = make_response(render_template('confidential/index.html'))
        response.headers.set("Access-Control-Allow-Credentials", "true")
        return response
