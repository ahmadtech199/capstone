import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie
import datetime

TOKEN_PRODUCER = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlBLRFh0NUVXY3l1aGxVcm9jZkR3TiJ9.eyJpc3MiOiJodHRwczovL2FobWFkMC5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTU5MDE2Nzc0Mjk1OTkxODI0OTMiLCJhdWQiOlsiY2Fwc3RvbmUiLCJodHRwczovL2FobWFkMC5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTk3MTE4MTk0LCJleHAiOjE1OTcxMjUzOTQsImF6cCI6Impjd1NOSzB0aVdTOWJ0WTAxblRHWnZzTTFydnBSMWc0Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.uuv5bi6qgdpM-1Be9SuF_3iJAZYcm5YmhggWRyijOs_Of5ciDJW7jr136Eyrl3ckCu52oSTaQs0-Fy8KxzFkW30YOrvPWaHoAi7llfBAD_PHfr5Iy3gY_MMaZtZvXapx3nNZJGLg7mfvn_BPZOnx7OdnMMdo4RjgJkgD5iGLrjeBdCWKBQWtDrAbmEC8hiAIheGuOR93beUf5pvPWSY6TLXAFFXFky5MZItxm13kLjrJInIV5vut98FpL0Tp1VAMPulf4e7cwk6t9nzsI2VyzWqkFnt2b7fexQEMy814suqjZuG9HV8r-Rh4jzpALptb5z7hdveP0O7B6htYeTs33w'


class CapstoneTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "Capstone_test"
        self.database_path = os.environ['TEST_DATABASE_URL']
        setup_db(self.app, self.database_path)

        self.new_actor = {
            'name': 'John Smith',
            'age': 34,
            'gender': 'male',
        }

        self.new_movie = {
            'actor_id': '2',
            'releaseDate': datetime.datetime(2022, 2, 22),
            'title': 'Contagion',
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        selection = Movie.query.filter(Movie.title == 'Contagion').all()
        for movie in selection:
            movie.delete()
        selection = Actor.query.filter(Actor.name == 'John Smith').all()
        for actor in selection:
            actor.delete()
        pass

    def test_get_all_actors(self):
        res = self.client().get('/actors', headers={
            'Authorization': TOKEN_PRODUCER}
        )
        data = res.get_json()

        selection = Actor.query.all()

        self.assertEqual(data['status'], True)
        self.assertEqual(data['actors'], [actor.format()
                                          for actor in selection])

    def test_post_actor(self):
        table_length = Actor.query.all()

        res = self.client().post('/actors/add', headers={
            'Authorization': TOKEN_PRODUCER},
            json=self.new_actor
        )

        data = res.get_json()

        self.assertEqual(data['status'], True)
        self.assertGreater(len(Actor.query.all()), len(table_length))

    def test_patch_actor(self):
        actor = Actor(
            name='Otilio',
            age=22,
            gender='male'
        )
        actor.id = 222
        actor.insert()

        res = self.client().patch('/actors/222', headers={
            'Authorization': TOKEN_PRODUCER},
            json={
                "name": "Otilio",
                "age": "54"
        }
        )
        data = res.get_json()

        actor = Actor.query.filter(Actor.id == 222).one_or_none()

        self.assertEqual(data['status'], True)
        self.assertEqual(actor.name, 'Otilio')

        actor.delete()

    def test_delete_actor(self):
        actor = Actor(
            name='Sean Conery',
            age=75,
            gender='male'
        )
        actor.id = 222
        actor.insert()

        res = self.client().delete('/actors/222', headers={
            'Authorization': TOKEN_PRODUCER},
        )

        data = res.get_json()
        selection = Actor.query.filter(Actor.id == 222).one_or_none()

        self.assertEqual(data['status'], True)
        self.assertEqual(selection, None)

    def test_get_all_movies(self):
        res = self.client().get('/movies', headers={
            'Authorization': TOKEN_PRODUCER}
        )
        data = res.get_json()

        selection = Movie.query.all()

        self.maxDiff = None

        self.assertEqual(data['status'], True)
        self.assertEqual(data['movies'], [movie.format()
                                          for movie in selection])

    def test_post_movie(self):
        table_length = Movie.query.all()

        res = self.client().post('/movies/add', headers={
            'Authorization': TOKEN_PRODUCER},
            json=self.new_movie
        )

        data = res.get_json()

        self.assertEqual(data['status'], True)
        self.assertGreater(len(Movie.query.all()), len(table_length))

    def test_patch_movie(self):
        movie = Movie(
            title='The cube',
            releaseDate=datetime.datetime(2022, 2, 22),
            actor_id='1'
        )
        movie.id = 222
        movie.insert()

        res = self.client().patch('/movies/222', headers={
            'Authorization': TOKEN_PRODUCER},
            json={
                "title": "avengers vs godzilla",
                "releaseDate": "2021-03-25 11:55:11.271041"
        }
        )

        data = res.get_json()
        selection = Movie.query.filter(Movie.id == 222).one_or_none()

        self.assertEqual(data['status'], True)
        self.assertEqual(selection.title, 'avengers vs godzilla')

        selection.delete()

    def test_delete_movie(self):
        movie = Movie(
            title='The cube',
            releaseDate=datetime.datetime(2022, 2, 22),
            actor_id='1'
        )
        movie.id = 222
        movie.insert()

        res = self.client().delete('/movies/222', headers={
            'Authorization': TOKEN_PRODUCER},
        )

        data = res.get_json()
        selection = Movie.query.filter(Movie.id == 222).one_or_none()

        self.assertEqual(data['status'], True)
        self.assertEqual(selection, None)

# Make the tests conveniently executable


if __name__ == "__main__":
    unittest.main()
