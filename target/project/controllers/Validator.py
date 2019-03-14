from project import app
from project.models.Dashboard import *
from flask import render_template, request, send_file, make_response, redirect, session
from xml.dom import minidom
from xml.dom.pulldom import parse
from xml.sax import make_parser
from xml.sax.handler import feature_external_ges

import os

from xml.dom.pulldom import START_ELEMENT, parseString

@app.route("/validator", methods=['GET'])
def validator():
    return render_template("validator/index.html")

@app.route("/validator/upload", methods=['GET', 'POST'])
def XML_validator():
    parser = make_parser()
    parser.setFeature(feature_external_ges, True)
    text_file = open("user_input.xml", "w+")
    text_file.write(request.form['books'])
    text_file.close()
    doc = parse("user_input.xml", parser=parser)
    try:
        for event, node in doc:
            if event == START_ELEMENT and node.localName == "books":
                doc.expandNode(node)
                nodes = node.toxml()
                return render_template("validator/index.html", nodes = nodes)
    except:
        return render_template("validator/index.html", error = "Validation failed")
    return render_template("validator/index.html", error = "Validation failed")
    

@app.route("/validator/getXML", methods=['GET', 'POST'])
def XML_download():
    fileName = request.form['example_file']
    file = open(fileName, "r") 
    response = make_response(send_file(fileName, attachment_filename=fileName))
    response.headers.set("Content-Type", "text/html; charset=utf-8")
    response.headers.set("Content-Disposition", "attachment; filename="+fileName)
    return response

@app.route("/validator/uploads", methods=['GET', 'POST'])
def XML_upload():
    if request.method == 'POST':
        file = request.files['file']
        print(file)
        if file:
            filename = file.filename
            file.save(filename)
            uploaded = "File was uploaded succesfully to the application, the staff members will process this information soon!"
            return render_template("validator/index.html",uploaded = uploaded)
        uploaded = "something went wrong, please try again. If the problem is repetitive please contact an administrator!"
        return render_template("validator/index.html",uploaded = uploaded)
    return render_template("validator/index.html")
    