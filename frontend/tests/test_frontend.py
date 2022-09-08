from flask import url_for
from flask_testing import TestCase
from datetime import date
import requests_mock
import pytest
# import the app's classes and objects
from application import app, db
from application.models import Exercises

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                DEBUG=True,
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        db.create_all()

        # Create test exercise
        sample1 = Exercises(exercise_name="Squat", exercise_sets="1", exercise_reps="1", exercise_accessories="Lunges, Bulgarian Split Squats and Leg Press", date_generated= date(2022, 9, 5))

        # save event to database
        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()


class TestViews(TestBase):
  
    def test_home_get(self):
        # mock values
        name = "Bench"
        sets = "2"
        reps = "2"
        accessories = "Military Press, Chest Flys and Tricep extensions"
        with requests_mock.Mocker() as m:
            m.get("http://exercise_generator_movement-api:5001/get_exercise", text=name)
            m.get("http://exercise_generator_sets-api:5003/get_sets", text=sets)
            m.get("http://exercise_generator_sets-api:5003/get_reps", text=reps)
            m.post("http://exercise_generator_exercise-api:5002/get_workout", text=accessories)
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Squat', response.data)
            self.assertIn(b'Bench', response.data)

    def test_hist_get(self):
        response = self.client.get(url_for('history'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Squat', response.data)