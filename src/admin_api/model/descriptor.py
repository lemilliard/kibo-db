from src.admin_api.utils.cleaner_utils import CleanerUtils


class Descriptor(object):

    def __init__(self, *args, **kwargs):
        self._name = kwargs.get("name", None)
        self._description = kwargs.get("description", None)
        self._system_name = kwargs.get("system_name", None)
        if self._system_name is None and self._name is not None:
            self._system_name = CleanerUtils.generate_system_name(self._name)

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

    def to_dict(self):
        _json_object = dict()
        _json_object["name"] = self._name
        _json_object["description"] = self._description
        _json_object["system_name"] = self._system_name
        return _json_object
