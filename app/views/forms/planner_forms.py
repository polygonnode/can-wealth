from flask_wtf import FlaskForm
from wtforms import StringField, TextField,PasswordField,SubmitField, validators,HiddenField
from wtforms.validators import DataRequired

class Survey_Form(FlaskForm):
    title = HiddenField()
    goal = HiddenField()
    age = HiddenField()
    income = HiddenField()
    down_payment = HiddenField()
    monthly_payment = HiddenField()

    def __init__(self,title, goal, age,income,down_payment,monthly_payment):
        self.title = title
        self.goal = goal
        self.age = age
        self.income = income
        self.down_payment = down_payment
        self.monthly_payment = monthly_payment
