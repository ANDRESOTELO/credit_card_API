#!/usr/bin/python3

def validate_card(card_number):
	""" Luhn algorithm to check Credit Card Number """
	inverted_number = card_number[::-1]
	number_to_luhn = inverted_number.replace(" ", "")
	luhn_list = []

	for index in range(len(number_to_luhn)):
		if index % 2 != 0:
			odd_index = int(number_to_luhn[index]) * 2
			if odd_index <= 9:
				luhn_list.append(odd_index)
			else:
				odd_index = str(odd_index)
				sum_odd = int(odd_index[0]) + int(odd_index[1])
				luhn_list.append(sum_odd)
		else:
			even_index = int(number_to_luhn[index])
			luhn_list.append(even_index)

	luhn_sum = sum(luhn_list)
	if luhn_sum % 10 == 0:
		return True
	else:
		return False