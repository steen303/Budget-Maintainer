from flask import Blueprint, request, jsonify
from db.db_categorie import DbCategorie
import json

api_categorie = Blueprint('api_categorie', __name__)


@api_categorie.route("all/", methods=['GET'])
def api_categories_get_all():
    db_cat = DbCategorie()
    return jsonify(db_cat.get_all().get_categories_json())


@api_categorie.route('categories/', methods=['POST'])
def api_categories_create():
    db_cat = DbCategorie()
    data = request.get_json(force=True) or {}
    if 'name' in data:
        db_cat.add_categorie(data['name'])
    return jsonify(db_cat.get_all().get_categories_json())

# TODO add post update categorie '/api/categories/1'
# TODO add delete categorie '/api/categories/&'
