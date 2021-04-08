from flask import Flask, render_template
from flask_cors import CORS

from api.api_category import api_category
from api.api_contact import api_contact
from api.api_transaction import api_income, api_expense

app = Flask(__name__, static_url_path='/')
CORS(app)


app.register_blueprint(api_category, url_prefix="/api/category")
app.register_blueprint(api_contact, url_prefix="/api/contact")
app.register_blueprint(api_income, url_prefix="/api/income")
app.register_blueprint(api_expense, url_prefix="/api/expense")

print(app.url_map)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Alexander'}
    return render_template('index.html', title='Home', user=user)


if __name__ == '__main__':
    app.run()
