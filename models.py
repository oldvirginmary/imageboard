# -*- coding: utf-8 -*-

from app import db

from datetime import datetime


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(256), nullable=False)
    content = db.Column(db.String(30000), nullable=False, unique=True)
    time = db.Column(db.DateTime, default=datetime.utcnow)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(3000), nullable=False, unique=True)

    article_id = db.Column(
        db.Integer,
        db.ForeignKey('article.id'),
        nullable=False,
        index=True
    )
    article = db.relationship(Article, foreign_keys=[article_id, ])
