from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager

PICS_FOLDER = os.path.join('static', 'images')     


app = Flask(__name__)

app.config['SECRET_KEY'] = '7dc999dc13b12c82360a4ca92411f6a9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['UPLOAD_FOLDER'] = PICS_FOLDER
db = SQLAlchemy(app)
login_manager = LoginManager(app)

ctx = app.app_context()                            # solves the outside of application context issue  (the code below didn't work)            
ctx.push()                                         # with app.app_context():
                                                   #     db.create_all()



from fitvidapphackathon.models import Workout

# Creating workout objects and adding them to the database
upper1 = Workout(name="Barbell Bench Press", length="Long", exercise_type="Weightlifting", intensity="High", instructor="Chris", link="https://www.youtube.com/watch?v=rT7DgCr-3pg")
upper2 = Workout(name="Dumbbell Incline Bench Press", length="Medium", exercise_type="Weightlifting", intensity="Medium", instructor="Chris",link="https://www.youtube.com/watch?v=8iPEnn-ltC8")
upper3 = Workout(name="Dumbbell Chest Flys", length="Medium", exercise_type="Weightlifting", intensity="Medium", instructor="Matt", link="https://youtu.be/eozdVDA78K0?t=33")
upper4 = Workout(name="Dumbbell Hammer Curls", length="Medium", exercise_type="Weightlifting", intensity="Medium", instructor="Emily", link="https://youtu.be/zC3nLlEvin4?t=22")
upper5 = Workout(name="Rope Pushdowns", length="Medium", exercise_type="Weightlifting", intensity="Medium", instructor="Monika", link="https://youtu.be/vB5OHsJ3EME?t=16")
upper6 = Workout(name="Bench Tricep Dips", length="Short", exercise_type="Weightlifting", intensity="Low", instructor="Chris", link="https://youtu.be/0326dy_-CzM?t=18")
upper7 = Workout(name="Barbell Military Press", length="Long", exercise_type="Weightlifting", intensity="High", instructor="Matt", link="https://www.youtube.com/watch?v=sBt6610fUiE")
upper8 = Workout(name="Dumbbell Front Raises", length="Short", exercise_type="Weightlifting", intensity="Low", instructor="Monika", link="https://youtu.be/gzDawZwDC6Y?t=5")
upper9 = Workout(name="Machine Lateral Raises", length="Short", exercise_type="Weightlifting", intensity="Low", instructor="Emily", link="https://www.youtube.com/watch?v=0FUpcwj_1z4")
upper10 = Workout(name="Lat Pulldowns", length="Medium", exercise_type="Weightlifting", intensity="Medium", instructor="Emily", link="https://youtu.be/1VcmFW5diOU?t=5")
upper11 = Workout(name="Rope Face Pulls", length="Medium", exercise_type="Weightlifting", intensity="Medium", instructor="Chris", link="https://www.youtube.com/watch?v=eFxMixk_qPQ")
upper12 = Workout(name="Cable Back Rows", length="Medium", exercise_type="Weightlifting", intensity="Medium", instructor="Matt", link="https://youtu.be/GZbfZ033f74?t=11")

db.session.add(upper1)
db.session.add(upper2)
db.session.add(upper3)
db.session.add(upper4)
db.session.add(upper5)
db.session.add(upper6)
db.session.add(upper7)
db.session.add(upper8)
db.session.add(upper9)
db.session.add(upper10)
db.session.add(upper11)
db.session.add(upper12)


db.create_all()
db.session.commit()








from fitvidapphackathon import routes 



