from src.main.admin_api.utils.cleaner_utils import CleanerUtils


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

    @staticmethod
    def from_json(_json: dict):
        _name = _json.get("name", None)
        _description = _json.get("description", None)
        _system_name = _json.get("system_name", None)
        return Descriptor(
            name=_name,
            description=_description,
            system_name=_system_name
        )

    def to_dict(self, _with_details: bool = False):
        _dict = dict()
        _dict["name"] = self._name
        _dict["description"] = self._description
        _dict["system_name"] = self._system_name
        return _dict
