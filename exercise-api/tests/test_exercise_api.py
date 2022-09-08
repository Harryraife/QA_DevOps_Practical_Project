from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import pytest
# import the app's classes and objects
from application import app

# Create the base class
class TestBase(TestCase):
    def create_app(self):
        return app


class TestViews(TestBase):

    def test_get_exercise(self):
        response = self.client.post(url_for('exercise'), json={"Exercise": "Squat", "Sets": "1", "Reps": "1"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Lunges, Bulgarian Split Squats and Leg Press', response.data)
