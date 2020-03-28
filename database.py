import datetime as dt

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Thought(db.Model):
    __tablename__ = 'thought'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Text(2000))  # around 400 (English) words
    # define foreign key
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = relationship('User', foreign_keys='Thoughts.author_id')

    def __init__(self, *args, **kw):
        super(Thought, self).__init__(*args, **kw)
        self.date = dt.datetime.now()

    def get_id(self):
        return self.id

    def get_author_id(self):
        return self.author_id



class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, *args, **kw):
        super(User, self).__init__(*args, **kw)

    def get_id(self):
        return self.id