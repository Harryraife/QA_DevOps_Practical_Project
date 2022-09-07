from application import app
from flask import Flask, request, Response

@app.route('/get_workout', methods = ['POST'])
def exercise():
    exercise_data = request.get_json()
    exercise_name = exercise_data["Exercise"]
    exercise_sets = exercise_data["Sets"]
    exercise_reps = exercise_data["Reps"]
    exercise_accessories = {"Squat":"Lunges, Bulgarian Split Squats and Leg Press", "Bench":"Military Press, Chest Flys and Tricep extensions", "Deadlift":"Bent over Row, Pull ups and Bicep Curls"}
    exercise = f"{exercise_accessories[exercise_name]}"
    return Response(exercise, mimetype='text/plain')
