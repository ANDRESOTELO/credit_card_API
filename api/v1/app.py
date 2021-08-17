#!/usr/bin/python3
""" Flask application """
from flask import Flask,  make_response, jsonify
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.route('/', methods=['GET'], strict_slashes=False)
def default_view():
	""" Defeault route """
	index_message = "Whale and Jaguar credit card validator\
		please use the (/card_validator/api/v1.0) prefix\
		after the port number to interact with the API"
	return make_response(index_message)


@app.errorhandler(404)
def not_found(error):
	"""
	404 error
	Response:
		404:
			a resource was not found
	"""
	return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
	""" Main function """
	app.run(host="0.0.0.0", debug=True, port=5000, threaded=True)