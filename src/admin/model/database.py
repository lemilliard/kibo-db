from .descriptor.database_descriptor import DatabaseDescriptor


class Database(object):

    def __init__(self, *args, **kwargs):
        if kwargs.get('descriptor') is not None:
            self.descriptor: DatabaseDescriptor = kwargs.get('descriptor')
        elif kwargs.get('name') is not None and kwargs.get('description') is not None:
            self.descriptor: DatabaseDescriptor = DatabaseDescriptor(
                name=kwargs.get('name'),
                description=kwargs.get('description')
            )
        else:
            self.descriptor: DatabaseDescriptor = None
        self.tables = []

    def get_descriptor(self) -> DatabaseDescriptor:
        return self.descriptor

    @staticmethod
    def from_descriptor(_descriptor: DatabaseDescriptor):
        return Database(
            descriptor=_descriptor
        )

    @staticmethod
    def from_file(file_path: str):
        return Database(
            descriptor=DatabaseDescriptor.from_file(file_path)
        )

    def save_file(self):
        self.descriptor.save_file()
