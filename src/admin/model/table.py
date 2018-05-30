from .descriptor.table_descriptor import TableDescriptor


class Table(object):

    def __init__(self, *args, **kwargs):
        if kwargs.get("descriptor") is not None:
            self.descriptor = kwargs.get("descriptor")
        elif kwargs.get("name") is not None and kwargs.get("description") is not None:
            self.descriptor = TableDescriptor(
                name=kwargs.get("name"),
                description=kwargs.get("description")
            )
        else:
            self.descriptor = None
        self.db_system_name = kwargs.get("db_system_name")

    def get_descriptor(self) -> TableDescriptor:
        return self.descriptor

    def get_db_system_name(self):
        return self.db_system_name

    @staticmethod
    def from_descriptor(_descriptor: TableDescriptor):
        return Table(descriptor=_descriptor)

    @staticmethod
    def from_file(_file_path: str):
        return Table(descriptor=TableDescriptor.from_file(_file_path))

    def to_file(self):
        self.descriptor.to_file()
