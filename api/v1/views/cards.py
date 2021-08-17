#!/usr/bin/python3
""" Handles cards information """
from api.v1.views import app_views
from flask import jsonify, abort
from data import all_cards
import luhn


@app_views.route('/cards', methods=['GET'], strict_slashes=False)
def get_cards():
	""" Retrieves the type of cards for the API """
	return jsonify(all_cards)


@app_views.route('/cards/<string:brand>', methods=['GET'], strict_slashes=False)
def get_brands(brand):
	"""
	Retrieves information about credit card brand
	---------------------------------------------
	Args:
		brand-> String of Credit card brand
	Return:
		brand_info-> JSON of brand information
	"""
	scheme_list = ["visa", "american", "diners", "mastercard"]
	if brand not in scheme_list:
		abort(404)
	brand_info = []
	for card in all_cards:
		if brand == card["scheme"]:
			brand_info.append(card)
	return jsonify(brand_info)


@app_views.route('/cards/validate/<string:card_number>', methods=['GET'], strict_slashes=False)
def get_card(card_number):
	"""
	Validate a card number
	------------------------
	Args:
		card_number-> number of the credit card
	Return:
		success-> When the number is valid
		error-> When the number is invalid
	"""
	if len(card_number) < 13:
		return jsonify({"error": "This is not a valid length card number, please check your card"}), 404
	if len(card_number) == 14 and luhn.validate_card(card_number) is False:
		for card in all_cards:
			if card_number[0:2] == card["MII"] or card_number[0:3] == card["MII"]:
				return jsonify({"error": "You have a Diners Club card, but the number is not valid"}), 404
		return jsonify({"error": "The credit card number is not valid"}), 404
	if len(card_number) == 15 and luhn.validate_card(card_number) is False:
		for card in all_cards:
			if card_number[0:2] == card["MII"]:
				return jsonify({"error": "You have an American Express card, but the number is not valid"}), 404
		return jsonify({"error": "The credit card number is not valid"}), 404
	if (len(card_number) == 16 or len(card_number) == 13) and luhn.validate_card(card_number) is True:
		for card in all_cards:
			if card_number[0] == card["MII"]:
				return jsonify({"success": "This is a valid " + card["brand"] + " credit card"})
	if luhn.validate_card(card_number) is True:
		for card in all_cards:
			if card_number[0:2] == card["MII"] or card_number[0:3] == card["MII"]:
				return jsonify({"success": "This is a valid " + card["brand"] + " credit card"})
	else:
		return jsonify({"error": "The credit card number is not valid"}), 404
