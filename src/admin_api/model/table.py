from .descriptor.table_descriptor import TableDescriptor


class Table(object):

    def __init__(self, *args, **kwargs):
        """Table constructor

        Args:
            descriptor (TableDescriptor): table descriptor
            name (str): table name
            description (str): table description
            db_system_name (str): database system name
        """
        if kwargs.get("descriptor") is not None:
            self.descriptor: TableDescriptor = kwargs.get("descriptor")
        elif kwargs.get("name") is not None and kwargs.get("description") is not None:
            self.descriptor: TableDescriptor = TableDescriptor(
                name=kwargs.get("name"),
                description=kwargs.get("description")
            )
        else:
            self.descriptor: TableDescriptor = None
        self.db_system_name = kwargs.get("db_system_name")

    def get_descriptor(self) -> TableDescriptor:
        """Get table descriptor

        Return:
            descriptor (TableDescriptor): table descriptor
        """
        return self.descriptor

    def get_db_system_name(self):
        """Get database system name

        Return:
            db_system_name (str): database system name
        """
        return self.db_system_name

    @staticmethod
    def from_descriptor(_descriptor: TableDescriptor):
        """Construct a Table object from a TableDescriptor

        Args:
            _descriptor (TableDescriptor): table descriptor

        """
        return Table(
            descriptor=_descriptor
        )

    @staticmethod
    def from_file(_file_path: str):
        """Construct a Table object from a TableDescriptor file

        Args:
            _file_path (str): table descriptor file path
        """
        return Table(
            descriptor=TableDescriptor.from_file(_file_path)
        )

    def save_file(self, _db_system_name: str):
        """Save TableDescriptor in a file

        Args:
            _db_system_name (str): database system name
        """
        self.descriptor.save_file(_db_system_name)

    def save_file(self):
        """Save TableDescriptor in a file"""
        self.descriptor.save_file(self.db_system_name)
