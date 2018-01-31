from flask import request, g, Blueprint, render_template, url_for, redirect

home = Blueprint('home', __name__)

#the route function tells the app which URL to bind to the function
@home.route("/")
def index():
    #just return the home page
    return redirect(url_for('planner.index'))
