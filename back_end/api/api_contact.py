from flask import Blueprint, request, jsonify
from db.db_contact import DbContact

api_contact = Blueprint('api_contact', __name__)


@api_contact.route("/api/contacts/all/", methods=['GET'])
def api_contacts_get_all():
    db_con = DbContact()
    return jsonify(db_con.get_all().get_contacts_json())


@api_contact.route('/api/contacts/', methods=['POST'])
def api_contacts_create():
    db_con = DbContact()
    data = request.get_json(force=True) or {}
    if 'name' in data:
        db_con.add_contact(data['name'])
    return jsonify(db_con.get_all().get_contacts_json())

# TODO add post update contacts '/api/contacts/Test'
# TODO add delete contacts '/api/contacts/Test'