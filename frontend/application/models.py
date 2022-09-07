from application import db

class Exercises(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String(50))
    exercise_sets = db.Column(db.String(10))
    exercise_reps = db.Column(db.String(10))
    exercise_accessories = db.Column(db.String(50))
    date_generated = db.Column(db.DateTime)
    def __str__(self):
        return f"{self.exercise_name}: {self.exercise_sets} set(s) of {self.exercise_reps} rep(s) with {self.exercise_accessories} to complete the workout - {self.date_generated}"
