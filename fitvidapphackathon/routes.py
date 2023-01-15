from flask import render_template, session, url_for, flash, redirect
from fitvidapphackathon import app
from fitvidapphackathon.forms import RegistrationForm, LoginForm
from fitvidapphackathon.models import Workout     # User
import random
import os


new_exercises = [
    {   'instructor': 'Matt',
        'exercise_name': 'Exercise Name 1',
        'content': 'First new exercise content',
        'date_posted': 'April 20, 2022'
    },
    {   'instructor': 'Emily',
        'exercise_name': 'Exercise Name 2',
        'content': 'Second new exercise content',
        'date_posted': 'May 3, 2022'
    },
    {   'instructor': 'Chris',
        'exercise_name': 'Exercise Name 3',
        'content': 'Third new exercise content',
        'date_posted': 'May 21, 2022'
    },
    {   'instructor': 'Monika',
        'exercise_name': 'Exercise Name 4',
        'content': 'Fourth new exercise content',
        'date_posted': 'June 1, 2022'
    }
]


@app.route("/")
@app.route("/home")
def home():
    pic_gym_1 = os.path.join(app.config['UPLOAD_FOLDER'], 'gym_1.png')
    pic_gym_2 = os.path.join(app.config['UPLOAD_FOLDER'], 'gym_2.png')
    return render_template('home.html', new_exercises=new_exercises, image_3 = pic_gym_1, image_4 = pic_gym_2)


@app.route("/about")
def about():
    pic_before = os.path.join(app.config['UPLOAD_FOLDER'], 'before_new.jpg')
    pic_after = os.path.join(app.config['UPLOAD_FOLDER'], 'after_new.jpg')
    return render_template("about.html", title='About', image_1 = pic_before, image_2 = pic_after)   # not sure how to not list the images manually



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Pelase check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/random_exercise", methods=['GET', 'POST'])     # Matt's original: @app.route("/")
def random_exercise():
    all_exercises = Workout.query.all()
    random_exercise = random.choice(all_exercises)
    personal_trainer = os.path.join(app.config['UPLOAD_FOLDER'], 'personal_trainer.png')
    return render_template('random_exercise.html', exercise=random_exercise, image_5 = personal_trainer)


@app.route("/logout")
def logout():
    flash("You have been logged out!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))


@app.route("/testing")
def testing():
    return render_template("testing.html", title='Testing')   

