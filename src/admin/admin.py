from flask import Blueprint
from flask import jsonify

from .endpoint.database_endpoint import DatabaseEndpoint
from .endpoint.table_endpoint import TableEndpoint

app_admin = Blueprint("app_admin", __name__)


@app_admin.route("/database", methods=["GET", "POST", "PUT"])
@app_admin.route("/database/<_db_system_name>", methods=["GET", "DELETE"])
def db_endpoint(_db_system_name=None):
    return jsonify(DatabaseEndpoint.process_request(_db_system_name))


@app_admin.route("/database/<_db_system_name>/table", methods=["GET", "POST", "PUT"])
@app_admin.route("/database/<_db_system_name>/table/<_tb_system_name>", methods=["GET", "DELETE"])
def tb_endpoint(_db_system_name, _tb_system_name=None):
    return jsonify(TableEndpoint.process_request(_db_system_name, _tb_system_name))
