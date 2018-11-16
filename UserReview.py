from flask import request
from flask_restful import Resource
from model import db, Review, ReviewSchema

reviews_schema = ReviewSchema(many=True)
review_schema = ReviewSchema()


class UserReview(Resource):
	def get(self):
		reviews = Review.query.all()
		reviews = reviews_schema.dump(reviews).data
		return {'status': 'success', 'user_reviews': reviews}, 200


	def post(self):
		json_data = request.get_json(force=True)
		if not json_data:
			return {'message': 'No input data provided'}, 400

		data, errors = review_schema.load(json_data)
		if errors:
			return {"status": "error", "data": errors}, 422
		product_id = Review.query.filter_by(id=data['product_id']).first()
		if not product_id:
			return {'status': 'error', 'message': 'review product not found'}, 400
		review = Review(
        	product_id=data['product_id'],
        	review=data['review']
        	)
		db.session.add(review)
		db.session.commit()

		result = review_schema.dump(review).data

		return {'status': "success", 'user_reviews': result}, 201


	def put(self):
		json_data = request.get_json(force=True)
		if not json_data:
			return {'message': 'No input data provided'}, 400
		data, errors = review_schema.load(json_data)
		if errors:
			return errors, 422
		review = Review.query.filter_by(id=data['id']).first()
		if not review:
			return {'message': 'Category does not exist'}, 400
		review.name = data['name']
		db.session.commit()

		result = review_schema.dump(review).data

		return { "status": 'success', 'data': result }, 204


	def delete(self):
		json_data = request.get_json(force=True)
		if not json_data:
			return {'message': 'No input data provided'}, 400
        
		data, errors = review_schema.load(json_data)
		if errors:
			return errors, 422
		review = Review.query.filter_by(id=data['id']).delete()
		db.session.commit()

		result = review_schema.dump(review).data

		return { "status": 'success', 'data': result}, 204