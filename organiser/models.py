from organiser import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(60), index=True, unique=True)
    email = db.Column(db.String(80), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    tasks = db.relationship('Task', backref='user', lazy='dynamic')
    about_me = db.Column(db.String(140))

    def todo(self):
        todo = Task.query.filter_by(phase = "todo", user_id=self.id).order_by(Task.timestamp.desc()).all()
        return todo 

    def doing(self):
        doing = Task.query.filter_by(phase = "doing", user_id=self.id).order_by(Task.timestamp.desc()).all()
        return doing

    def done(self):
        done = Task.query.filter_by(phase = "done", user_id=self.id).order_by(Task.timestamp.desc()).all()
        return done

    def count(self):
        count = Task.query.filter_by(phase = "done", user_id=self.id).count()
        return count 

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Username: {}>'.format(self.username)

@login.user_loader
def load_user(id):
    return User.query.get(id)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    body = db.Column(db.String(120))
    phase = db.Column(db.String(6))
    importance = db.Column(db.String(1))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    deadline = db.Column(db.DateTime)

    def __repr__(self):
        return '<title: {}, body: {}, phase: {}, importance: {}, deadline: {}>'.format(self.title, self.body, self.phase, self.importance, self.deadline)