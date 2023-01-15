from flask import render_template, session, url_for, flash, redirect
from fitvidapphackathon import app, db
from fitvidapphackathon.forms import RegistrationForm, LoginForm
from fitvidapphackathon.models import User, Workout     
import random
import os
from flask_login import login_user, current_user


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
    if current_user.is_authenticated:
        return redirect (url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)    # the password should pass the hashed password --> to do
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!. You can now log in', 'success') 
        # flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect (url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@ourwebsite.com' and form.password.data == 'password':
            user = User.query.filter_by(email=form.email.data).first()
            if user and user.password:    # add and hashed password --> research bcrypt
                    login_user(user, remember=form.remember.data )
                    return redirect(url_for('home'))
            else:
                flash('Login Unsuccessful. Please check email and password', 'danger')
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


@app.route("/workouts_by_instructor")   # needs to be changed to show only one column i.e. links to the videos
def workouts_by_instructor():

    all_workouts_Matt = Workout.query.filter_by(instructor='Matt').all()
    return render_template("workouts_by_instructor.html", title='Workouts By Instructor', all_workouts_Matt=all_workouts_Matt)   

