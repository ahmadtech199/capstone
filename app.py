import os
from flask import Flask, request, abort, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actor, Movie
import datetime
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers', 'Content-Type,Authorization,true'
        )
        response.headers.add(
            'Access-Control-Allow-Methods', 'GET,POST,DELETE,OPTIONS,PATCH'
        )
        return response

    @app.route('/')
    def main():
        greeting = "Hi There"

        return greeting

    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors(payload):
        selection = Actor.query.all()

        actors = []

        for actor in selection:
            actors.append(actor.format())

        return jsonify({
            'status': True,
            'actors': actors
        })

    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies(payload):
        selection = Movie.query.all()

        movies = []

        for movie in selection:
            movies.append(movie.format())

        return jsonify({
            'status': True,
            'movies': movies
        })

    @app.route('/actors/<id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, id):
        selection = Actor.query.get(id)

        if not selection:
            abort(404)

        try:
            selection.delete()
        except Exception as e:
            print('it could not be deleted', e)

        return jsonify({
            'status': True,
            'actor': id
        })

    @app.route('/movies/<id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def movie(payload, id):
        selection_id = Movie.query.get(id)

        if not selection_id:
            abort(404)

        try:
            selection = Movie.query.filter(
                Movie.title == selection_id.title).all()
            for movie in selection:
                movie.delete()
        except Exception as e:
            print('it could not be deleted', e)

        return jsonify({
            'status': True,
            'movie': selection_id.title
        })

    @app.route('/actors/add', methods=['POST'])
    @requires_auth('post:actors')
    def post_actor(payload):
        res = request.get_json()

        if not res:
            abort(400)

        try:
            actor = Actor(
                name=res['name'],
                age=res['age'],
                gender=res['gender']
            )
            actor.insert()

        except Exception as e:
            print('we couldnt create the object', e)
            abort(500)
        return jsonify({
            'status': True,
            'actor': [actor.format()]
        })

    @app.route('/movies/add', methods=['POST'])
    @requires_auth('post:movies')
    def post_movies(payload):
        res = request.get_json()

        movies = []
        if not res:
            abort(400)
        try:
            index = 0
            for movie in res['actor_id']:
                movie = Movie(
                    title=res['title'],
                    releaseDate=datetime.datetime.strptime(
                        res['releaseDate'], '%a, %d %b %Y %H:%M:%S %Z'),
                    actor_id=res['actor_id'][index]
                )
                movies.append(movie.format())
                movie.insert()
                index += 1

        except Exception as e:
            print('we couldnt create the object. Reason :', e)
            abort(500)

        return jsonify({
            'status': True,
            'movie': movies
        })

    @app.route('/actors/<id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def patch_actors(payload, id):
        res = request.get_json()

        if not res:
            abort(404)

        actor = Actor.query.get(id)

        try:
            if 'name' in res:
                actor.name = res['name']
            if 'age' in res:
                actor.age = res['age']
            if 'gender' in res:
                actor.gender = res['gender']

            actor.update()

        except Exception as e:
            abort(500)

        return jsonify({
            'status': True,
            'actor': [actor.format()]
        })

    @app.route('/movies/<id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def patch_movies(payload, id):
        res = request.get_json()

        if not res:
            abort(404)

        movie = Movie.query.get(id)

        try:
            if 'title' in res:
                movie.title = res['title']
            if 'releaseDate' in res:
                movie.releaseDate = res['releaseDate']
            if 'actor_id' in res:
                movie.actor_id = res['actor_id']

            movie.update()

        except Exception as e:
            print('we couldnt create the object. Reason :', e)
            abort(500)

        return jsonify({
            'status': True,
            'movie': [movie.format()]
        })

    # Error Handling

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable."
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "The server can not find the requested resource."
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowed"
        }), 405

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "You are no authorized."
        }), 401

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
