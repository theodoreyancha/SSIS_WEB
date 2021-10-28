from flask import Flask, render_template, redirect, url_for, request, session
from flask_session import Session
import mysql.connector

app = Flask(__name__)



@app.route("/")
def mainmenu():
    return render_template("mainmenu.html")

@app.route("/student/",methods=["post","get"])
def student():
    return render_template("inputs.html")

@app.route("/course/",methods=["post","get"])
def course():
    return render_template("course.html")

@app.route("/college/",methods=["post","get"])
def college():
    return render_template("college.html")