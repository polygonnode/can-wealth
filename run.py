from app import create_app

app = create_app()


from app.models import db
@app.before_first_request
def init():
    db.create_all()
