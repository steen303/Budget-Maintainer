from flask import Blueprint, request, jsonify
from db.db_transaction import DbTransaction

api_income = Blueprint('api_income', __name__)


@api_income.route("/api/income/all", methods=['GET'])
def api_income_get_all():
    db_inc = DbTransaction()
    return jsonify(db_inc.get_all_income().get_json())


@api_income.route("/api/income/<int:year>/<int:month>/", methods=['POST'])
def api_income_post(year, month):
    db_inc = DbTransaction()
    data = request.get_json(force=True) or {}
    if 'day' in data and 'category' in data and 'fromWho' in data and 'description' in data and 'value' in data:
        db_inc.add_income(year, month, int(data['day']), data['description'], data['value'],
                          data['category'], data['fromWho'])
    return jsonify(db_inc.get_all_income().get_json())


@api_income.route("/api/income/<int:year>/<int:month>/", methods=['GET'])
def api_income_get(year, month):
    db_inc = DbTransaction()
    return jsonify(db_inc.get_by_month(year, month).get_json())
