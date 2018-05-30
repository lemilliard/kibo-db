from .descriptor import table_descriptor


class Table:

    def __init__(self, name, description):
        self.descriptor = table_descriptor(name, description)

    def get_descriptor(self):
        return self.descriptor
