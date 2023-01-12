from marshmallow import Schema, fields

from database.setup_db import db


# ----------------------------------------------------------------
# Post model and Schema
class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    poster_name = db.Column(db.String)
    poster_avatar = db.Column(db.String)
    pic = db.Column(db.String)
    content = db.Column(db.String)
    views_count = db.Column(db.Integer)
    likes_count = db.Column(db.Integer)


class PostSchema(Schema):
    id = fields.Int()
    poster_name = fields.Str()
    poster_avatar = fields.Str()
    pic = fields.Str()
    content = fields.Str()
    views_count = fields.Int()
    likes_count = fields.Int()


# ----------------------------------------------------------------
# Comment model and Schema
class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    commenter_name = db.Column(db.String)
    comment = db.Column(db.String)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    post = db.relationship('Post')


class CommentSchema(Schema):
    id = fields.Int()
    commenter_name = fields.Str()
    comment = fields.Str()
    post_id = fields.Int()


# ----------------------------------------------------------------
# Bookmarks model and schema
class Bookmark(db.Model):
    __tablename__ = 'bookmarks'

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    post = db.relationship('Post')


class BookmarkSchema(Schema):
    id = fields.Int()
    post_id = fields.Int()
