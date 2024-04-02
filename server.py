import os
import csv
from flask import Flask, render_template,request,redirect

#flask --app server run
#flask --app server run --debug
app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route("/submit_form", methods=["POST","GET"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
    return redirect("/thankyou.html")  #render_template("index.html")

def save_file(data):
    with open("database.txt","a+") as file:
        file.write(str(data))

def write_to_csv(data):
    with open("database.csv","a+") as db:
        csv_writter = csv.writer(db,delimiter=",",quoting=csv.QUOTE_MINIMAL)
        csv_writter.writerow(data.values())

# @app.route("/index.html")
# def my_home2():
#     return render_template("index.html")

# @app.route("/about.html")
# def my_about():
#     return render_template("about.html")

# @app.route("/components.html")
# def my_components():
#     return render_template("components.html")

# @app.route("/contact.html")
# def my_contact():
#     return render_template("contact.html")

# @app.route("/work.html")
# def my_work():
#     return render_template("work.html")

# @app.route("/works.html")
# def my_works():
#     return render_template("works.html")