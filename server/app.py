from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_migrate import Migrate
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from datetime import timedelta,datetime

from models import db, User, Event, Registration

app = Flask(__name__)

# Configure app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key_here'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Enable CORS for all routes
CORS(app)

# Define resources
class Home(Resource):
    def get(self):
        return {'message': 'Welcome to our Events Management Application'}

api = Api(app)
api.add_resource(Home, '/')

class Login(Resource):
    def post(self):
        email = request.json.get('email', None)
        password = request.json.get('password', None)

        if not email or not password:
            return {'message': 'Both email and password are required'}, 400

        user = User.query.filter_by(email=email).first()

        if not user or not bcrypt.check_password_hash(user.password_hash, password):
            return {'message': 'Invalid credentials'}, 401

        access_token = create_access_token(identity=user.id)
        return {'access_token': access_token}, 200

api.add_resource(Login, '/login')

class Events(Resource):
    def get(self):
        events = [event.to_dict() for event in Event.query.all()]
        return jsonify(events)
    def post(self):
        try:
            title = request.json['title']
            description = request.json['description']
            date_str = request.json['date']
            location = request.json['location']
            no_of_registrations = request.json['no_of_registrations']
            creator_id = request.json['creator_id']

            # Convert date string to a date object
            date = datetime.strptime(date_str, '%Y-%m-%d').date()

            new_event = Event(
                title=title,
                description=description,
                date=date,
                location=location,
                no_of_registrations=no_of_registrations,
                creator_id=creator_id
            )

            db.session.add(new_event)
            db.session.commit()

            return new_event.to_dict(), 201

        except KeyError as e:
            return {'error': f'Missing required field: {str(e)}'}, 400
        except ValueError as e:
            return {'error': f'Invalid date format: {str(e)}'}, 400
        except Exception as e:
            return {'error': str(e)}, 500

api.add_resource(Events, '/events')

class RegistrationResource(Resource):
    @jwt_required()
    def post(self):
        try:
            event_id = request.json.get('event_id')
            user_id = get_jwt_identity()

            if not event_id:
                return {'message': 'Event ID is required'}, 400

            new_registration = Registration(event_id=event_id, user_id=user_id)
            db.session.add(new_registration)
            db.session.commit()

            event = Event.query.get(event_id)
            event.no_of_registrations = len(event.registrations)
            db.session.commit()

            return {'message': 'Registered successfully', 'count': event.no_of_registrations}, 201

        except Exception as e:
            return {'error': str(e)}, 500

api.add_resource(RegistrationResource, '/registrations')

@app.route('/users', methods=['POST'])
def register_user():
    data = request.get_json()

    name = data.get('name')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not name or not username or not email or not password:
        return jsonify({'message': 'Missing required fields'}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    new_user = User(name=name, username=username, email=email, password_hash=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400

    return jsonify({'message': 'User registered successfully'}), 201

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)
