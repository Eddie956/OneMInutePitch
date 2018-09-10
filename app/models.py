from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    pitch =db.relationship('Pitch', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    like = db.relationship('Like', backref='user', lazy='dynamic')
    dislike = db.relationship('Dislike', backref='user', lazy='dynamic')

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'
    '''
    class that define my pitches
    '''
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    category = db.Column(db.String(255))
    pitch = db.Column(db.DateTime, default=datetime.utcnow)

    comment = db.relationship('Comment', backref='pitch', lazy='dynamic')
    like = db.relationship('Like', backref='pitch', lazy='dynamic')
    dislike = db.relationship('Dislike', backref='pitch', lazy='dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Pitch {self.id}'


class Comment(db.Model):
    __tablename__ = 'comment'
    '''
    class that define my comments
    '''
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    comment = db.Column(db.String(255))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Comment {self.id}'
    

class Like(db.Model):
    __tablename__ = 'likes'
    '''
    class that takes number of upvote in aparticular pitch
    '''
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    likes = db.Column(db.Integer,default=1)

    def save_like(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Like {self.id}'


class Dislike(db.Model):
    __tablename__ = 'dislike'
    '''
    class that define my comments
    '''
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    dislikes = db.Column(db.Integer,default=1)

    def save_Dislike(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Dislike {self.id}'


class PhotoProfile(db.Model):
    __tablename__ = 'profile_photos'

    id = db.Column(db.Integer, primary_key=True)
    pic_path = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
