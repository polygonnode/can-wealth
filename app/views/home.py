from flask import request, g, Blueprint, render_template

home = Blueprint('home', __name__)

#the route function tells the app which URL to bind to the function
@home.route("/")
def index():
    #just return the home page
    return render_template("home/index.html")


@home.route("/about")
def about():
    return render_template("home/about.html",x=True)
