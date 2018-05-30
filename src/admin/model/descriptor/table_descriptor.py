from src.admin.utils.cleaner_utils import *


class TableDescriptor:

    def __init__(self, name, description):
        self._name = name
        self._system_name = generate_clean_name(name)
        self._description = description
