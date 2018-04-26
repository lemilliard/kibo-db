from flask import Blueprint
from flask import jsonify
from flask import request

from . import endpoints

app_admin = Blueprint("app_admin", __name__)


@app_admin.route("/database", methods=["GET", "POST"])
def database_endpoint():
    return jsonify(endpoints.database.endpoint())


@app_admin.route("/database/<_dt_system_name>", methods=["GET", "PUT", "DELETE"])
def database_with_system_name_endpoint(_dt_system_name):
    return jsonify(endpoints.database_with_system_name.endpoint(_dt_system_name))


@app_admin.route("/database/<_dt_system_name>/table", methods=["GET", "POST"])
def database_table_endpoint(_dt_system_name):
    return jsonify(endpoints.database_table.endpoint(_dt_system_name))


@app_admin.route("/database/<_dt_system_name>/table/<_tb_system_name>", methods=["GET", "PUT", "DELETE"])
def database_table_with_system_name_endpoint(_dt_system_name, _tb_system_name):
    return jsonify(endpoints.database_table_with_system_name.endpoint(_dt_system_name, _tb_system_name))


def get_body():
    if request.json is None:
        return False
    return request.json
