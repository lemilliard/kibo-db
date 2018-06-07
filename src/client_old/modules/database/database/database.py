from src.admin.utils.database_utils import DatabaseUtils


def get_database(_system_name: str):
    descriptor = DatabaseUtils.get_database_descriptor(_system_name)
    if descriptor is not False:
        return descriptor.__dict__
    return False


data = {
    "page_name": "Database"
}

methods = {
    "get_database": get_database,
    "create_database": DatabaseUtils.create_database
}

on_open = [
]
