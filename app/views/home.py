from flask import request, g, Blueprint, render_template, url_for, redirect
from app.models import Feedback, db
home = Blueprint('home', __name__)

#the route function tells the app which URL to bind to the function
@home.route("/")
def index():
    #just return the home page
    return redirect(url_for('planner.index'))


@home.route("/feedback", methods=["POST"])
def feedback_route():
    email = request.form["email"]
    print(email)
    body = request.form["body"]
    feedback = Feedback(email,body)
    db.session.add(feedback)
    db.session.commit()
    return redirect(url_for('planner.index'))
