from flask import request, g, Blueprint, render_template, url_for
from app.views.forms.planner_forms import Survey_Form
planner = Blueprint('planner', __name__)


@planner.route("/survey", methods=["GET","POST"])
def index():
    form = Survey_Form(request.form)
    error = None

    if request.method == "POST":
        print(form.data)
        print("survey was posted too reidecting you to result")
        return url_for('planer.result',id=1234)
    #just return the home page
    return render_template("planner/survey.html",form=form)



@planner.route("/results")
def results():
<<<<<<< HEAD
    survey_id = request.args.get('id')
    if False:
        #find the surevey and run the financeCalculations

        title = "Test Plan"
        test_goal = 30000
        test_down_payment = 7000
        test_monthly_payment = 2500
        render_template("planner/results.html")

=======
>>>>>>> 330a169c477700d07051004b098a4b853d0a2173


    return redirect(url_for('planner.index'))




#supportying functions
def financeCalculations(goal, down, monthly):
    remainder = goal - down
    in_account = down
    period = 0
    while(goal >= monthly): # calculate end of every monthly
        #end of month
        in_account = (in_acount * 1.02) +(monthly -5)
