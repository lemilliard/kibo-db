from src.admin.utils.database_utils import DatabaseUtils


def get_databases():
    data["databases"] = []
    descriptors = DatabaseUtils.get_databases_descriptor()
    for descriptor in descriptors:
        data["databases"].append(descriptor.__dict__)


data = {
    "page_name": "Databases",
    "databases": []
}

methods = {
    "get_databases": get_databases
}

on_open = [
    "get_databases"
]
