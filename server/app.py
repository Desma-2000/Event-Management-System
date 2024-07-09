#!/usr/bin/env python3

# Standard library imports
# Remote library imports
from flask import request, make_response, jsonify
from flask_restful import Resource
from flask_migrate import Migrate
import os
# Local imports
from config import app, db, api
# Add your model imports
from models import User, Event

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")


migrate = Migrate(app, db)

class Home(Resource):
    def get(self):
        response_body = {
            'message': 'Welcome to our Events Management Application'
        }
        return make_response(response_body, 200)

api.add_resource(Home, '/')

class Login(Resource):
    def get(self):
      pass
        
api.add_resource(Login, '/login')

class UserRegistration(Resource):
    def post(self):
        try:
            new_user = User (
            first_name = request.json['first_name'],
            last_name = request.json['last_name'],
            email = request.json['email'],
            username = request.json['username'],
            password = request.json['password'],
        )
            db.session.add(new_user)
            db.session.commit()

            user_dict = new_user.to_dict()

            return make_response(user_dict, 201)
        
        except ValueError:
            response_body = {
                'error': 'Could not create user'
            }
            return make_response(response_body, 400)

api.add_resource(UserRegistration, '/register_user')

class Events(Resource):
    def get(self):
        events = [event.to_dict() for event in Event.query.all()]

        response = make_response(events, 200)
        return response
    def post():
        try:
            new_event = Event(
                name = request.json['name'],
                location = request.json['location'],
                date = request.json['date'],
                speaker = request.json['speaker']
            )
            db.session.add(new_event)
            db.session.commit()

            event_dict = new_event.to_dict()
            response = make_response(event_dict, 201)

            return response
        except ValueError:
            response_body = {
                'error': 'error occurred'
            }
            return make_response(response_body, 400)
        
api.add_resource(Events, '/events')
        
class EventsByID(Resource):
    def get(self,id):
        event = Event.query.filter_by(id=id).first()
        if event:
            event_dict = event.to_dict()
            return make_response(event_dict, 200)
        else:
            response_body = {
                'message' : 'Event does not exist! Check the id again.'
            }

            return make_response(response_body, 404)
        
    def delete(self, id):
        event = Event.query.filter_by(id=id).first()
        if event:
            db.session.delete()
            db.session.commit()

            response_body = {
                'message': 'Event deleted Successfully'
            }
            return make_response(response_body, 200)
        else:
            response_body = {
                'message' : 'Event does not exist! Check the id again.'
            }

            return make_response(response_body, 404)
        
    def patch(self,id):
         event = Event.query.filter_by(id=id).first()
         if event:
            try:
                for attr in request.json:
                    setattr(event, attr, request.json.get(attr))

                db.session.add()
                db.session.commit()

                event_dict = event.to_dict
                return make_response(event_dict, 200)
            
            except ValueError:
                response_body = {
                    'error': 'error occured'
                }
         else:
            response_body = {
                'message' : 'Event you are trying to Edit does not exist! Check the id again.'
            }

            return make_response(response_body, 404)
         
api.add_resource(EventsByID, '/events/<int:id>')


if __name__ == '__main__':
    app.run(port=5555, debug=True)

