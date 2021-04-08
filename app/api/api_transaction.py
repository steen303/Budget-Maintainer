from flask import Blueprint, request, jsonify
from db.db_transaction import DbTransaction

api_income = Blueprint('api_income', __name__)
api_expense = Blueprint('api_expense', __name__)


@api_income.route("/all/", methods=['GET'])
def api_income_get_all():
    db_transaction = DbTransaction()
    return jsonify(db_transaction.get_all_income().get_json())


@api_income.route("/<int:year>/<int:month>/", methods=['GET'])
def api_income_get(year, month):
    db_transaction = DbTransaction()
    return jsonify(db_transaction.get_by_month(year, month, False).get_json())


@api_income.route("/<int:year>/<int:month>/", methods=['POST'])
def api_income_post(year, month):
    db_transaction = DbTransaction()
    data = request.get_json(force=True) or {}
    if 'day' in data and 'category' in data and 'contact' in data and 'description' in data and 'value' in data:
        db_transaction.add_income(year, month, int(data['day']), data['description'], data['value'],
                                  data['category'], data['contact'])
    return jsonify(db_transaction.get_by_month(year, month, False).get_json())


@api_expense.route("/all/", methods=['GET'])
def api_expense_get_all():
    db_transaction = DbTransaction()
    return jsonify(db_transaction.get_all_expense().get_json())


@api_expense.route("/<int:year>/<int:month>/", methods=['GET'])
def api_expense_get(year, month):
    db_transaction = DbTransaction()
    return jsonify(db_transaction.get_by_month(year, month, True).get_json())


@api_expense.route("/<int:year>/<int:month>/", methods=['POST'])
def api_expense_post(year, month):
    print(request.get_json(force=True))
    db_transaction = DbTransaction()
    data = request.get_json(force=True) or {}
    if 'day' in data and 'category' in data and 'contact' in data and 'description' in data and 'value' in data:
        db_transaction.add_expense(year, month, int(data['day']), data['description'], data['value'],
                                   data['category'], data['contact'])
    return api_expense_get(year, month)
