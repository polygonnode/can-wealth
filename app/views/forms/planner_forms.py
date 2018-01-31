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

    
