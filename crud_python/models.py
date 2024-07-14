# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()
# class Book(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), nullable=False)
#     author = db.Column(db.String(120), nullable=False)
#     issue_date = Column(Date, nullable=True)
#     return_date = Column(Date, nullable=True)
#     def to_dict(self):
#         return {
#             'id': self.id,
#             'title': self.title,
#             'author': self.author,
#             'issue_date': self.issue_date,
#             'return_date': self.return_date
#         }
# def init_db(app):
#     db.init_app(app)
#     with app.app_context():
#         db.create_all()










from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    issue_date = db.Column(db.Date, nullable=True)
    return_date = db.Column(db.Date, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'issue_date': self.issue_date,
            'return_date': self.return_date
        }

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
