from flask import Blueprint
from .data import config

client_api = Blueprint("client_api", __name__)


@client_api.route("/switch_night_mode")
def switch_night_mode():
    return config.switch_night_mode()
