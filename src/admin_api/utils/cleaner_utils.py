import re
import unidecode


class CleanerUtils(object):

    @staticmethod
    def generate_clean_name(_name):
        _clean_name = re.sub("'", " ", _name)
        _clean_name = unidecode.unidecode(_clean_name)
        _clean_name = re.sub("[^0-9a-zA-Z ]", "", _clean_name)
        _clean_name = re.sub("\s+", " ", _clean_name)
        return _clean_name

    @staticmethod
    def generate_system_name(_clean_name):
        _db_system_name = _clean_name.lower()
        _db_system_name = _db_system_name.replace(" ", "_")
        return _db_system_name
