from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    events = db.relationship('Event', backref='creator', lazy=True)
    registrations = db.relationship('Registration', backref='user', lazy=True)

    # Serialization rules
    serialize_rules = ('-password_hash', '-events.creator', '-registrations.user')

    def __repr__(self):
        return f"<User {self.username}>"

class Event(db.Model, SerializerMixin):
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(128), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    registrations = db.relationship('Registration', backref='event', lazy=True)

    # Serialization rules
    serialize_rules = ('-creator.events', '-registrations.event')

    def __repr__(self):
        return f"<Event {self.title} at {self.location} on {self.date}>"

    @staticmethod
    def validate_date(date):
        if date < datetime.utcnow():
            raise ValueError("The event date cannot be in the past.")

class Registration(db.Model, SerializerMixin):
    __tablename__ = 'registrations'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    comment = db.Column(db.Text, nullable=True)
    registered_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Serialization rules
    serialize_rules = ('-user.registrations', '-event.registrations')

    def __repr__(self):
        return f"<Registration {self.id} by User {self.user_id} for Event {self.event_id}>"

