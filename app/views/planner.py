from flask import request, g, Blueprint, render_template

planner = Blueprint('planner', __name__)


@planner.route("/survey")
def index():
    #just return the home page
    return render_template("planner/survey.html")



@planner.route("/results")
def index():


    return render_template("planner/results.html")
