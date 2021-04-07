from flask import Flask, render_template, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_url_path='/')
CORS(app)

from api.api_categorie import api_categorie
from api.api_contact import api_contact
from api.api_income import api_income

app.register_blueprint(api_categorie, url_prefix="/api/categorie")
app.register_blueprint(api_contact, url_prefix="/api/contact")
app.register_blueprint(api_income, url_prefix="/api/income")

print(app.url_map)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Alexander'}
    return render_template('index.html', title='Home', user=user)


if __name__ == '__main__':
    app.run()

