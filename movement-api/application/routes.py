from application import app
from flask import Flask, request, Response
import random

@app.route('/get_exercise', methods=['GET'])
def movement():
    exercise_name = random.choice(["Squat", "Bench", "Deadlift"])
    return Response(exercise_name, mimetype='text/plain')