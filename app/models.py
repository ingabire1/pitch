from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# class News:
#     '''
#     News class to define News Objects
#     '''
#
#     def __init__(self,id,name,description,url,language,country):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.url = url
#         self.language = language
#         self.country = country

# class Arti:
#     '''
#     News class to define Articles Objects
#     '''
#
#     def __init__(self,id,name,title,poster,description,publishedAt,content,url):
#         self.id = id
#         self.name = name
#         self.title = title
#         self.poster = poster
#         self.description = description
#         self.publishedAt = publishedAt
#         self.content = content
#         self.url = url

    # def save_review(self):
    #     Review.all_reviews.append(self)
    #
    #
    # @classmethod
    # def clear_reviews(cls):
    #     Review.all_reviews.clear()
    #
    # @classmethod
    # def get_reviews(cls,id):
    #
    #     response = []
    #
    #     for review in cls.all_reviews:
    #         if review.news_id == id:
    #             response.append(review)
    #
    #     return response
    #

# class Review:
#
#     all_reviews = []
#
#     def __init__(self,news_id,title,urlToImage,review):
#         self.news_id = news_id
#         self.title = title
#         self.urlToImage = urlToImage
#         self.description = description
#
#
#     def save_review(self):
#         Review.all_reviews.append(self)
#
#
#     @classmethod
#     def clear_reviews(cls):
#         Review.all_reviews.clear()
#
#     @classmethod
#     def get_reviews(cls,id):
#
#         response = []
#
#         for review in cls.all_reviews:
#             if review.news_id == id:
#                 response.append(review)
#
#         return response


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    # role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    # reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

# class Role(db.Model):
#     __tablename__ = 'roles'
#
#     id = db.Column(db.Integer,primary_key = True)
#     name = db.Column(db.String(255))
#     users = db.relationship('User',backref = 'role',lazy="dynamic")
#
#     def __repr__(self):
#         return f'User {self.name}'

# class Review(db.Model):
#
#     __tablename__ = 'reviews'
#
#     id = db.Column(db.Integer,primary_key = True)
#     movie_id = db.Column(db.Integer)
#     movie_title = db.Column(db.String)
#     image_path = db.Column(db.String)
#     movie_review = db.Column(db.String)
#     posted = db.Column(db.DateTime,default=datetime.utcnow)
#     user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
#
#     def save_review(self):
#         db.session.add(self)
#         db.session.commit()
#
#     @classmethod
#     def get_reviews(cls,id):
#         reviews = Review.query.filter_by(movie_id=id).all()
#         return reviews
