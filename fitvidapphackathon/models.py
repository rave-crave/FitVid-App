from datetime import datetime
from fitvidapphackathon import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='jpeg')
    password = db.Column(db.String(60), nullable=False)
    new_exercises = db.relationship('Exercise', backref='instructor', lazy=True)

    def  __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)    # Matt's ID line:   _id = db.Column("id",db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)       # Matt's line:    name = db.Column(db.String(50))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    length = db.Column(db.String(10), nullable=False) #  <-- Matt's; added nullable
    exercise_type = db.Column(db.String(20), nullable=False)   # <-- Matt's; added nullable + deleted one 'n' in Column
    intensity = db.Column(db.String(20), nullable=False)  # <-- Matt's; added nullable
    link = db.Column(db.String(200), nullable=False) # <-- Matt's; added nullable
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def  __repr__(self):
        return f"Exercise('{self.name}', '{self.length}', '{self.exercise_type}', '{self.intensity}')"     # to add this? '{self.date_posted}'

    # # Matt's code block that goes into the Exercise class (his name: Workout class): 
    # def __init__(self, name, date_posted, length, exercise_type, intensity, content, link):     # added: date_posted and content
    #     self.name = name
    #     self.date_posted = date_posted
    #     self.length = length
    #     self.exercise_type = exercise_type
    #     self.intensity = intensity
    #     self.content = content
    #     self.link = link

# def init_db():
#     db.create_all()

# if __name__ == '__main__':
#     init_db()