from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from api import api_categorie, api_contact, api_income

app.register_blueprint(api_categorie, url_prefix="/api/categorie")
app.register_blueprint(api_contact, url_prefix="/api/contact")
app.register_blueprint(api_income, url_prefix="/api/income")
print(app.url_map)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('layout.html', title='Home', user=user)

if __name__ == '__main__':
    app.run()
