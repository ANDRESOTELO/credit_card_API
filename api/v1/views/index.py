#!/usr/bin/python3
""" Index and status information """
from api.v1.views import app_views
from flask import jsonify, abort
from data import all_cards
import luhn


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
	""" Status of the API """
	return jsonify({'status': 'OK'})