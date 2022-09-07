from application import app, db
from flask import Flask, request, render_template, url_for
from application.models import Exercises
import requests
from datetime import date


# home route
@app.route('/', methods = ['GET'])
def home():
    exercise_name = requests.get('http://movement-api:5001/get_exercise')
    exercise_sets = requests.get('http://sets-api:5003/get_sets')
    exercise_reps = requests.get('http://sets-api:5003/get_reps')
    exercise_data = requests.post('http://exercise-api:5002/get_workout', json = {"Exercise": exercise_name.text, "Sets": exercise_sets.text, "Reps": exercise_reps.text})
    workout = Exercises(exercise_name = exercise_name.text, exercise_sets = exercise_sets.text, exercise_reps = exercise_reps.text, exercise_accessories = exercise_data.text, date_generated = date.today())
    db.session.add(workout)
    db.session.commit()
    past5 = Exercises.query.order_by(Exercises.id.desc()).limit(5).all()
    return render_template('index.html', workout=workout, past5 = past5)

@app.route('/history', methods=['GET'])
def history():
    exercises_history = Exercises.query.all()
    return render_template('history.html', exercises_history = exercises_history)
