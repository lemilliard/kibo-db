from src.admin.utils.cleaner_utils import CleanerUtils


class Descriptor(object):

    def __init__(self, *args, **kwargs):
        self._name = kwargs.get("name")
        self._description = kwargs.get("description")
        self._system_name = kwargs.get("system_name", CleanerUtils.generate_system_name(self._name))

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_system_name(self):
        return self._system_name

    def set_system_name(self, system_name):
        self._system_name = system_name
