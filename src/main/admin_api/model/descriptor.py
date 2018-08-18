class Descriptor(object):

    def __init__(self, *args, **kwargs):
        from src.main.common.utils.cleaner_utils import CleanerUtils

        self.name = kwargs.get("name", None)
        self.description = kwargs.get("description", None)
        self.system_name = kwargs.get("system_name", None)
        if self.system_name is None and self.name is not None:
            self.system_name = CleanerUtils.generate_system_name(self.name)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_system_name(self):
        return self.system_name

    def set_system_name(self, system_name):
        self.system_name = system_name

    @staticmethod
    def from_json(_json: dict):
        name = _json.get("name", None)
        description = _json.get("description", None)
        system_name = _json.get("system_name", None)
        return Descriptor(
            name=name,
            description=description,
            system_name=system_name
        )

    def to_dict(self, with_details: bool = False):
        _dict = dict()
        _dict["name"] = self.name
        _dict["description"] = self.description
        _dict["system_name"] = self.system_name
        return _dict
