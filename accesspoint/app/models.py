from app import db

class Idiot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    password = db.Column(db.String(64), index=True)
    user_agent = db.Column(db.String(256), index=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)
