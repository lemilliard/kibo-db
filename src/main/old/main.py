from flask import Flask
from src.main.old.admin_api.main import admin_api
from src.main.old.query_api.main import query_api
from src.main.old.config import active_config

app = Flask(__name__)
app.config["DEBUG"] = active_config.debug
app.register_blueprint(admin_api, url_prefix="/admin")
app.register_blueprint(query_api, url_prefix="/query")

app.run(host=active_config.host, port=active_config.port)
