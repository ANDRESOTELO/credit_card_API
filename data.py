#!/usr/bin/python3
"""Information about cards"""

all_cards = [
		{"id": 1, "scheme": "visa", "brand": "Visa","MII": "4","type": "Credit", "validate": {"length": 16, "luhn": True}, "icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Visa_Inc._logo.svg/556px-Visa_Inc._logo.svg.png"},
		{"id": 2, "scheme": "mastercard", "brand": "Master Card","MII": "51","type": "Credit", "validate": {"length": 16, "luhn": True}, "icon": "https://cam.mastercard.com/content/dam/mccom/global/logos/logo-mastercard-mobile.svg"},
		{"id": 3, "scheme": "mastercard", "brand": "Master Card","MII": "52","type": "Credit", "validate": {"length": 16, "luhn": True}, "icon": "https://cam.mastercard.com/content/dam/mccom/global/logos/logo-mastercard-mobile.svg"},
		{"id": 4, "scheme": "mastercard", "brand": "Master Card","MII": "53","type": "Credit", "validate": {"length": 16, "luhn": True}, "icon": "https://cam.mastercard.com/content/dam/mccom/global/logos/logo-mastercard-mobile.svg"},
		{"id": 4, "scheme": "mastercard", "brand": "Master Card","MII": "54","type": "Credit", "validate": {"length": 16, "luhn": True}, "icon": "https://cam.mastercard.com/content/dam/mccom/global/logos/logo-mastercard-mobile.svg"},
		{"id": 5, "scheme": "mastercard", "brand": "Master Card","MII": "55","type": "Credit", "validate": {"length": 16, "luhn": True}, "icon": "https://cam.mastercard.com/content/dam/mccom/global/logos/logo-mastercard-mobile.svg"},
		{"id": 6, "scheme": "american", "brand": "American Express","MII": "34","type": "Credit", "validate": {"length": 15, "luhn": True}, "icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/American_Express_logo_%282018%29.svg/1200px-American_Express_logo_%282018%29.svg.png"},
		{"id": 7, "scheme": "american", "brand": "American Express","MII": "37","type": "Credit", "validate": {"length": 15, "luhn": True}, "icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/American_Express_logo_%282018%29.svg/1200px-American_Express_logo_%282018%29.svg.png"},
		{"id": 8, "scheme": "diners", "brand": "Diners Club International","MII": "36","type": "Credit", "validate": {"length": 14, "luhn": True}, "icon": "https://1000marcas.net/wp-content/uploads/2020/08/logo-Diners-Club-International.png"},
		{"id": 9, "scheme": "diners", "brand": "Diners Club International","MII": "38","type": "Credit", "validate": {"length": 14, "luhn": True}, "icon": "https://1000marcas.net/wp-content/uploads/2020/08/logo-Diners-Club-International.png"},
		{"id": 10, "scheme": "diners", "brand": "Diners Club International","MII": "300","type": "Credit", "validate": {"length": 14, "luhn": True}, "icon": "https://1000marcas.net/wp-content/uploads/2020/08/logo-Diners-Club-International.png"},
		{"id": 11, "scheme": "diners", "brand": "Diners Club International","MII": "301","type": "Credit", "validate": {"length": 14, "luhn": True}, "icon": "https://1000marcas.net/wp-content/uploads/2020/08/logo-Diners-Club-International.png"},
		{"id": 11, "scheme": "diners", "brand": "Diners Club International","MII": "302","type": "Credit", "validate": {"length": 14, "luhn": True}, "icon": "https://1000marcas.net/wp-content/uploads/2020/08/logo-Diners-Club-International.png"},
		{"id": 11, "scheme": "diners", "brand": "Diners Club International","MII": "303","type": "Credit", "validate": {"length": 14, "luhn": True}, "icon": "https://1000marcas.net/wp-content/uploads/2020/08/logo-Diners-Club-International.png"},
		{"id": 11, "scheme": "diners", "brand": "Diners Club International","MII": "304","type": "Credit", "validate": {"length": 14, "luhn": True}, "icon": "https://1000marcas.net/wp-content/uploads/2020/08/logo-Diners-Club-International.png"},
		{"id": 11, "scheme": "diners", "brand": "Diners Club International","MII": "305","type": "Credit", "validate": {"length": 14, "luhn": True}, "icon": "https://1000marcas.net/wp-content/uploads/2020/08/logo-Diners-Club-International.png"}
]