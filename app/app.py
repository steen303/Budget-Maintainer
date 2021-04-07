from flask import Flask
from flask_cors import CORS

from api.api_categorie import api_categorie
from api.api_contact import api_contact
from api.api_income import api_income

app = Flask(__name__)
CORS(app)
app.register_blueprint(api_categorie)
app.register_blueprint(api_contact)
app.register_blueprint(api_income)
print(app.url_map)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
