from flask import Flask, render_template, request, redirect
from fun import *
from json_utils import *

app = Flask(__name__)
@app.route("/",methods=["POST","GET"])

def homepage():
    if request.method == "POST":
        print(request.form["name"],request.form["age"],request.form["course"],request.form["address"])
        register_stud(request.form["name"],request.form["age"],request.form["course"],request.form["address"])
    return render_template("homepage.html",data = read_json())

@app.route("/delete/<sno>")

def remove(sno):
    delete_stud(sno)
    return redirect("/")

@app.route("/update/<sno>",methods=["POST","GET"])
def update(sno):
    if request.method == "POST":
        update_stud(sno,request.form["name"],request.form["age"],request.form["course"],request.form["address"])
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True,host = "0.0.0.0")
