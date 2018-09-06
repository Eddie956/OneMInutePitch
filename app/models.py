from app import create_app, db
from app.models import User


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User)


if __name__ == '__main__':
    manager.run()
