from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    pass_secure = db.Column(db.String(255))

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
    __table__name = 'pitches'
    '''
    class that define my pitches
    '''
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.integer,db.Foreign_key('users_id'))
    category = db.Column(db.String(255))
    pitch = db.Column(db.String(255))

    def __repr__(self):
        return f'Pitch {self.id}'


class Comment(db.Model):
    __table__name = 'comment'
    '''
    class that define my comments
    '''
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.integer, db.Foreign_key('users_id'))
    pitch_id = db.Column(db.integer, db.Foreign_key('pitches_id'))
    pitch = db.Column(db.String(255))

    def __repr__(self):
        return f'Pitch {self.id}'
    

# class Like(db.Model):
#     __table__name = 'likes'
#     '''
#     class that takes number of upvote in aparticular pitch
#     '''
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.integer, db.Foreign_key('users_id'))
#     pitch_id = db.Column(db.integer, db.Foreign_key('pitches_id'))
#     likes = db.Column(db.Integer,default=1)

#     def __repr__(self):
#         return f'Pitch {self.id}'


# class Dislike(db.Model):
#     __table__name = 'dislike'
#     '''
#     class that define my comments
#     '''
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.integer, db.Foreign_key('users_id'))
#     pitch_id = db.Column(db.integer, db.Foreign_key('pitches_id'))
#     dislikes = db.Column(db.Integer,default=1)

#     def __repr__(self):
#         return f'Pitch {self.id}'
