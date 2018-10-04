import sys


class ConfigDev(object):
    debug = True
    host = "0.0.0.0"
    port = 8500
    files_directory = "../../databases"
    data_directory = "data"
    index_directory = "index"
    json_separators = None
    json_indent = 4


class ConfigProd(ConfigDev):
    debug = False
    files_directory = "databases"


active_config = ConfigDev

if getattr(sys, "frozen", False):
    active_config = ConfigProd
