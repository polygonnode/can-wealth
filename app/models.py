from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    goal = db.Column(db.Integer)
    age = db.Column(db.Integer)
    income = db.Column(db.Integer)
    down_payment = db.Column(db.Integer)
    monthly_payment = db.Column(db.Integer)



    def __init__(self,title,goal,age,income,down_payment,monthly_payment):
        self.title = title
        self.goal = goal
        self.age = age
        self.income = income
        self.down_payment = down_payment
        self.monthly_payment = monthly_payment


    def __repr__(self):
            return "< Surevy "+ str(self.id) + " >"
