from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = '7dc999dc13b12c82360a4ca92411f6a9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


# from fitvidapphackathon.models import Exercise

# upper1 = Exercise(name="Barbell Bench Press", length="Long", exercise_type="Weightlifting", intensity="High", link="https://www.youtube.com/watch?v=rT7DgCr-3pg")
# upper2 = Exercise(name="Dumbbell Incline Bench Press", length="Medium", exercise_type="Weightlifting", intensity="Medium", link="https://www.youtube.com/watch?v=8iPEnn-ltC8")
# upper3 = Exercise(name="Dumbbell Chest Flys", length="Medium", exercise_type="Weightlifting", intensity="Medium", link="https://youtu.be/eozdVDA78K0?t=33")
# upper4 = Exercise(name="Dumbbell Hammer Curls", length="Medium", exercise_type="Weightlifting", intensity="Medium", link="https://youtu.be/zC3nLlEvin4?t=22")
# upper5 = Exercise(name="Rope Pushdowns", length="Medium", exercise_type="Weightlifting", intensity="Medium", link="https://youtu.be/vB5OHsJ3EME?t=16")
# upper6 = Exercise(name="Bench Tricep Dips", length="Short", exercise_type="Weightlifting", intensity="Low", link="https://youtu.be/0326dy_-CzM?t=18")
# upper7 = Exercise(name="Barbell Military Press", length="Long", exercise_type="Weightlifting", intensity="High", link="https://www.youtube.com/watch?v=sBt6610fUiE")
# upper8 = Exercise(name="Dumbbell Front Raises", length="Short", exercise_type="Weightlifting", intensity="Low", link="https://youtu.be/gzDawZwDC6Y?t=5")
# upper9 = Exercise(name="Machine Lateral Raises", length="Short", exercise_type="Weightlifting", intensity="Low", link="https://www.youtube.com/watch?v=0FUpcwj_1z4")
# upper10 = Exercise(name="Lat Pulldowns", length="Medium", exercise_type="Weightlifting", intensity="Medium", link="https://youtu.be/1VcmFW5diOU?t=5")
# upper11 = Exercise(name="Rope Face Pulls", length="Medium", exercise_type="Weightlifting", intensity="Medium", link="https://www.youtube.com/watch?v=eFxMixk_qPQ")
# upper12 = Exercise(name="Cable Back Rows", length="Medium", exercise_type="Weightlifting", intensity="Medium", link="https://youtu.be/GZbfZ033f74?t=11")

# db.session.add(upper1)
# db.session.add(upper2)
# db.session.add(upper3)
# db.session.add(upper4)
# db.session.add(upper5)
# db.session.add(upper6)
# db.session.add(upper7)
# db.session.add(upper8)
# db.session.add(upper9)
# db.session.add(upper10)
# db.session.add(upper11)
# db.session.add(upper12)

# db.session.commit()

# db.create_all()
# db.session.commit()


# @app.before_first_request
# def create_tables():
#     db.create_all()



with app.app_context():
    db.create_all()


from fitvidapphackathon import routes 



