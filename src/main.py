from flask import Flask
from src.admin_api.main import admin_api
from src.query_api.main import query_api

from src.config import Config

app = Flask(__name__)
app.config["DEBUG"] = True
app.register_blueprint(admin_api, url_prefix="/admin")
app.register_blueprint(query_api, url_prefix="/query")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=Config.port)
