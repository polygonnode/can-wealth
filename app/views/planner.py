from flask import request, g, Blueprint, render_template, url_for, redirect
from app.views.forms.planner_forms import Survey_Form
from app.models import Survey, db
planner = Blueprint('planner', __name__)


@planner.route("/survey", methods=["GET","POST"])
def index():
    form = Survey_Form(request.form)
    error = None
    if request.method == "POST":
        goal = int(request.form["goal"].replace(",", ""))
        age = int(request.form["age"].replace(",", ""))
        income = int(request.form["income"].replace(",", ""))
        down_payment = int(request.form["down_payment"].replace(",", ""))
        monthly_payment = int(request.form["monthly_payment"].replace(",", ""))
        survey = Survey(request.form["title"],goal,age,income,down_payment,monthly_payment)
        db.session.add(survey)
        db.session.commit()
        return redirect(url_for('planner.results',id=survey.id))
    #just return the home page
    return render_template("planner/survey.html",form=form)



@planner.route("/results")
def results():

    survey_id = request.args.get('id')

    if survey_id:
        survey = Survey.query.filter_by(id=int(survey_id)).first()

        if survey:
            months = financeCalculations(survey.goal,survey.down_payment,survey.monthly_payment)
            return render_template("planner/results.html",months=months[0],survey=survey,months_total=len(months[0]),saved=months[1])

        #find the surevey and run the financeCalculations
    return redirect(url_for('planner.index'))




#supportying functions
def financeCalculations(goal, down, monthly):
    their_contribution = down
    remainder = goal - down
    in_account = down
    period = 1
    return_list = []
    intrest = (in_account * 0.00166666667)
    our_contribution = intrest
    account_change = intrest
    remainder = remainder - (intrest)
    in_account = down + intrest
    while(remainder >= monthly): # calculate end of every monthly
      #end of month
      in_account = in_account + (monthly -5)
      their_contribution += (monthly-5)
      intrest = (in_account * 0.00166666667)
      in_account += intrest
      our_contribution = our_contribution + intrest  # for our tracking
      remainder = goal - in_account

      return_list.append([period,their_contribution,in_account,""])

      period = period + 1
    # now the remainder
    if(remainder > 0):

        in_account += remainder
        their_contribution += remainder
        return_list.append([period,their_contribution,in_account,""])
    print(our_contribution)
    return return_list, ((our_contribution/goal)*period)
