from src.main.old.admin_api.model.database import Database
from src.main.old.admin_api.model.table import Table


class DescriptorFactory(object):
    """Factory de génération de descripteurs"""

    table_name = 'TableName'
    database_name = 'DatabaseName'
    description = 'Description'

    @classmethod
    def create_database_with_name(cls, name: str) -> Database:
        return Database(name=name, description=cls.description)

    @classmethod
    def create_database(cls) -> Database:
        return cls.create_database_with_name(cls.database_name)

    @classmethod
    def create_database_list(cls, size: int):
        database_list = []
        for i in range(0, size):
            database_list.append(cls.create_database_with_name(cls.database_name + str(i)))
        return database_list

    @classmethod
    def create_database_list_with_database(cls, database: Database, size: int):
        database_list = []
        for i in range(0, size):
            database_list.append(database)
        return database_list

    @classmethod
    def create_database_name_list(cls, size: int):
        database_name_list = []
        for i in range(0, size):
            database_name_list.append(cls.database_name + str(i))
        return database_name_list

    @classmethod
    def create_table(cls):
        return Table(name=cls.table_name, description=cls.description)
