from flask import Blueprint
from flask import jsonify

from .endpoint.database_endpoint import DatabaseEndpoint
from .endpoint.system_endpoint import SystemEndpoint
from .endpoint.table_endpoint import TableEndpoint
from .endpoint.field_endpoint import FieldEndpoint

admin_api = Blueprint("admin_api", __name__)


@admin_api.route("/database/connect/<_db_system_name>", methods=["POST"])
def system_endpoint(_db_system_name: str):
    return jsonify(SystemEndpoint.connect(_db_system_name))


@admin_api.route("/database", methods=["GET", "POST"])
@admin_api.route("/database/<db_system_name>", methods=["GET", "PUT", "DELETE"])
def db_endpoint(db_system_name: str = None):
    return jsonify(DatabaseEndpoint.process_request(db_system_name=db_system_name))


@admin_api.route("/database/<db_system_name>/table", methods=["GET", "POST"])
@admin_api.route("/database/<db_system_name>/table/<tb_system_name>", methods=["GET", "PUT", "DELETE"])
def tb_endpoint(db_system_name: str, tb_system_name: str = None):
    return jsonify(TableEndpoint.process_request(db_system_name=db_system_name, tb_system_name=tb_system_name))


@admin_api.route("/database/<_db_system_name>/table/<_tb_system_name>/field", methods=["GET", "POST"])
@admin_api.route("/database/<_db_system_name>/table/<_tb_system_name>/field/<_fd_system_name>",
                 methods=["GET", "PUT", "DELETE"])
def fd_endpoint(_db_system_name: str, _tb_system_name: str, _fd_system_name: str = None):
    return jsonify(FieldEndpoint.process_request(db_system_name=_db_system_name, tb_system_name=_tb_system_name, fd_system_name=_fd_system_name))
