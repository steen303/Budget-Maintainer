from app import app
from api import api_categorie, api_contact, api_income

app.register_blueprint(api_categorie, url_prefix="/api/categorie")
app.register_blueprint(api_contact, url_prefix="/api/contact")
app.register_blueprint(api_income, url_prefix="/api/income")
print(app.url_map)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return '''
<html>
    <head>
        <title>Home Page - Budget</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''