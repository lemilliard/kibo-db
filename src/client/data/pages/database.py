from src.admin.utils.database_utils import DatabaseUtils


def get_databases():
    data["databases"] = []
    descriptors = DatabaseUtils.get_databases_descriptor()
    for descriptor in descriptors:
        data["databases"].append(descriptor.__dict__)
    return data["databases"]


def get_database(_system_name: str):
    descriptor = DatabaseUtils.get_database_descriptor(_system_name)
    if descriptor is not False:
        return descriptor.__dict__
    return False


data = {
    "page_name": "Databases",
    "databases": []
}

methods = {
    "get_databases": get_databases,
    "get_database": get_database
}

on_open = [
    "get_databases"
]
