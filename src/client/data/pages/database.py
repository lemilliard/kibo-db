from src.admin.utils.database_utils import DatabaseUtils


def get_databases():
    databases = []
    descriptors = DatabaseUtils.get_databases_descriptor()
    for descriptor in descriptors:
        databases.append(descriptor.__dict__)
    return databases


def get_database(_system_name: str):
    descriptor = DatabaseUtils.get_database_descriptor(_system_name)
    if descriptor is not False:
        return descriptor.__dict__
    return False


data = {
    "page_name": "Databases",
    "databases": get_databases()
}

methods = {
    "get_database": get_database
}
