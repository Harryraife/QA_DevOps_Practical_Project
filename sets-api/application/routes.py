from application import app
from flask import Flask, request, Response
import random

@app.route('/get_sets', methods=['GET'])
def sets():
    exercise_sets = str(random.randint(1,4))
    return Response(exercise_sets, mimetype='text/plain')

@app.route('/get_reps', methods=['GET'])
def reps():
    exercise_reps = str(random.randint(1,12))
    return Response(exercise_reps, mimetype='text/plain')