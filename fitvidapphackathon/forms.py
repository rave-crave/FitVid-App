from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from fitvidapphackathon.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email', 
                            validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                                     validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')


    def validate_username(self, username):                                         # Creating exceptions for trying to use the same username (and email below)
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is taken. Please choose a different one.')


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email', 
                            validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')


class PostForm(FlaskForm):
    length = StringField('Length', validators=[DataRequired()] )
    intensity = StringField('Intensity', validators=[DataRequired()] )
    exercise_type = StringField('Exercise Type', validators=[DataRequired()] )
    submit = SubmitField('Post')