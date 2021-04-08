from flask import Blueprint, request, jsonify
from db.db_categorie import DbCategory

api_category = Blueprint('api_category', __name__)


@api_category.route("/all/", methods=['GET'])
def api_category_get_all():
    db_cat = DbCategory()
    return jsonify(db_cat.get_all().get_categories_json())


@api_category.route('/', methods=['POST'])
def api_category_create():
    db_cat = DbCategory()
    data = request.get_json(force=True) or {}
    if 'name' in data:
        db_cat.add_category(data['name'])
    return jsonify(db_cat.get_all().get_categories_json())

# TODO add post update categorie '/api/categories/1'
# TODO add delete categorie '/api/categories/&'
