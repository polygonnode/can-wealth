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
        print("survey was posted too reidecting you to result")
        return redirect(url_for('planner.results',id=survey.id))
    #just return the home page
    return render_template("planner/survey.html",form=form)



@planner.route("/results")
def results():

    survey_id = request.args.get('id')
    if False:
        #find the surevey and run the financeCalculations
        render_template("planner/results.html")


    return redirect(url_for('planner.index'))




#supportying functions
def financeCalculations(goal, down, monthly):
    remainder = goal - down
    in_account = down
    period = 0
    our_contribution = 0
    return_list = []
    while(remainder >= monthly): # calculate end of every monthly
      #end of month
      our_contribution = our_contribution + (in_account * 0.0017)
      account_change = (in_account * 1.0017)  + (monthly -5)
      remainder = remainder - (account_change - in_account)
      in_account = account_change
      period = period + 1
      print("=========")
      print(in_account)
      print(our_contribution)
      return_list.append([period,in_account,our_contribution])
      print(return_list)
    # now the remainder
    if(remainder > 0):
      period += 1
      in_account = in_account + remainder
      remainder = 0

    print(in_account)
    print(period)
    print((our_contribution/in_account)*period)



    return(return_list)
