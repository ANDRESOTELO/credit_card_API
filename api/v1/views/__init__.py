#!/usr/bin/python3
"""
Blueprint for API
------------------
URL_prefix:
    /card_validator/api/v1.0
"""
from flask import Blueprint
prefix = "/card_validator/api/v1.0"
app_views = Blueprint('app_views', __name__, url_prefix=prefix)

from api.v1.views.index import *
from api.v1.views.cards import *
