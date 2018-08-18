class CleanerUtils(object):

    @staticmethod
    def generate_clean_name(name):
        import re
        import unidecode

        clean_name = re.sub("'", " ", name)
        clean_name = unidecode.unidecode(clean_name)
        clean_name = re.sub("[^0-9a-zA-Z ]", "", clean_name)
        clean_name = re.sub("\s+", " ", clean_name)
        return clean_name

    @staticmethod
    def generate_system_name(clean_name):
        system_name = clean_name.lower()
        system_name = system_name.replace(" ", "_")
        return system_name
