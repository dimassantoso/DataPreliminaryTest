from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Review(db.Model):
    __tablename__ = 'user_review'
    id 			= db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id	= db.Column(db.String(11), nullable=False)
    product_id	= db.Column(db.String(11), nullable=False)
    user_id		= db.Column(db.String(11), nullable=False)
    rating		= db.Column(db.Float, nullable=False)
    review 		= db.Column(db.String(250), nullable=False)
    created_at 	= db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    update_at 	= db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, order_id, product_id, user_id, rating, review):
    	self.order_id		= order_id
    	self.product_id 	= product_id
    	self.user_id		= user_id
    	self.rating			= rating
    	self.review 		= review
        

class ReviewSchema(ma.Schema):
	id 			= fields.Integer()
	order_id	= fields.String(required=True)
	product_id	= fields.String(required=True)
	user_id		= fields.String(required=True)
	rating		= fields.Float(required=True)
	review		= fields.String(required=True)
	created_at	= fields.DateTime()
	update_at	= fields.DateTime()