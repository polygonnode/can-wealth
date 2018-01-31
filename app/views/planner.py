from flask import request, g, Blueprint, render_template, url_for
from app.views.forms.planner_forms import Survey_Form
planner = Blueprint('planner', __name__)


@planner.route("/survey", methods=["GET","POST"])
def index():
    #form = Survey_Form(request.form)
    error = None
    if request.method == "POST":
        return url_for('planer.result',id=1234)
    #just return the home page
    return render_template("planner/survey.html")



@planner.route("/results")
def results():
    title = "Test Plan"
    test_goal = 30000
    test_down_payment = 7000
    test_monthly_payment = 2500



    return render_template("planner/results.html")




#supportying functions
def financeCalculations(goal, down, monthly):
    remainder = goal - down
    in_account = down
    period = 0
    while(goal >= monthly): # calculate end of every monthly
        #end of month
        in_account = (in_acount * 1.02) +(monthly -5)
