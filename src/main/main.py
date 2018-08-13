from flask import Flask
from src.main.admin_api.main import admin_api
from src.main.query_api.main import query_api

from src.main.config import Config

app = Flask(__name__)
app.config["DEBUG"] = True
app.register_blueprint(admin_api, url_prefix="/admin")
app.register_blueprint(query_api, url_prefix="/query")

app.run(host="0.0.0.0", port=Config.port)
