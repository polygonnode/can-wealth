from flask import request, g, Blueprint, render_template

planner = Blueprint('planner', __name__)

#the route function tells the app which URL to bind to the function
@planner.route("/survey")
def index():
    #just return the home page
    return render_template("planner/survey.html")
