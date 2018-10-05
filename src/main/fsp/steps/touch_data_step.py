def execute(**params):
    # _files = _function()
    # _unique_key_values = sous_step_1(_files)
    # sous_step_2(_unique_key_values)
    return 'touch_data'


def sous_step_1(_files):
    _unique_key_values = []
    for _file in _files:
        _unique_key_value = get_unique_key_values_id(_file)
        if _unique_key_value not in _unique_key_values:
            _unique_key_values.append(_unique_key_value)
        update_file(_file)
    return _unique_key_values


def get_unique_key_values_id(_file):
    return 0


def update_file(_file):
    pass


def sous_step_2(_unique_key_values):
    return delete_indexes(_unique_key_values)


def delete_indexes(_unique_key_values):
    pass
