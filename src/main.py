from flask import Flask
from src.admin.admin import app_admin
from src.client_old.client_api import client_api

app = Flask(__name__, template_folder="client_old/modules")
app.static_folder = 'client_old/modules'
app.config["DEBUG"] = True
app.register_blueprint(app_admin, url_prefix="/admin")
app.register_blueprint(client_api, url_prefix="/client_old")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
