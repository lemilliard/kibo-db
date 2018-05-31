from flask import Blueprint

from . import client
from .data import base

client_api = Blueprint("client_api", __name__)


@client_api.route("/api/switch_night_mode")
def switch_night_mode():
    return base.switch_night_mode()


@client_api.route('/')
@client_api.route('/<path:page>')
def client_endpoint(page=None):
    return client.client_endpoint(page)
