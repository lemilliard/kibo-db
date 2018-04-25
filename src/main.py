from flask import Flask
from src.admin.admin import app_admin
from src.client.client_api import client_api

app = Flask(__name__, template_folder="client/view")
app.config['DEBUG'] = True
app.register_blueprint(app_admin, url_prefix='/admin')
app.register_blueprint(client_api, url_prefix='/client')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
