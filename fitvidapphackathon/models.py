# from datetime import datetime
from fitvidapphackathon import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




class User(db.Model, UserMixin):
    """
    Represents a user with an id, username, email, default picture(*to be changed in the future), password and workouts
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='jpeg')
    password = db.Column(db.String(60), nullable=False)
    workouts = db.relationship('Workout', lazy=True)     # research many-to-many relationship + check whether to add add 'back_populated' or use the older 'backref'

    def  __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Workout(db.Model):
    """
    Represents a workout with an id, name, email, length, exercise_type, intensity, instructor, link and user_id, which serves as a foreign key
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)    #_id   
    name = db.Column(db.String(50), nullable=False)
    length = db.Column(db.String(10), nullable=False)
    exercise_type = db.Column(db.String(20), nullable=False)
    intensity = db.Column(db.String(20), nullable=False)
    instructor = db.Column(db.String(20), nullable=False)
    link = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def  __repr__(self):
        return f"Exercise('{self.name}', '{self.length}', '{self.exercise_type}', '{self.intensity}','{self.instructor}''{self.link}')"   



# class Exercise(db.Model):       for the future --> individual exercises that can comprise a customised workout plan; add instructor

#     id = db.Column(db.Integer, primary_key=True)    # Matt's ID line:   _id = db.Column("id",db.Integer, primary_key = True);       
#     name = db.Column(db.String(100), nullable=False)       # Matt's line:    name = db.Column(db.String(50))
#     # date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     length = db.Column(db.String(10), nullable=False) #  <-- Matt's; added nullable
#     exercise_type = db.Column(db.String(20), nullable=False)   # <-- Matt's; added nullable + deleted one 'n' in Column
#     intensity = db.Column(db.String(20), nullable=False)  # <-- Matt's; added nullable
#     link = db.Column(db.String(200), nullable=False) # <-- Matt's; added nullable
#     # content = db.Column(db.Text, nullable=False)
#     # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def  __repr__(self):
#         return f"Exercise('{self.name}', '{self.length}', '{self.exercise_type}', '{self.intensity}','{self.link}')"     


  