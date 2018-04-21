def build_condition(_object):
	_condition = _object.condition
	return "WHERE " + build_conditions(_condition)


def build_conditions(_condition, _operator=None):
	_str = ""
	if isinstance(_condition, list):
		print("Liste")
		for _c in _condition:
			_str += " " + _operator + " ("
			_str += build_conditions(_c)
			_str += ")"
	else:
		for i in range(0, len(_condition._fields)):
			print(_condition._fields[i])
			if _condition._fields[i] == 'OR' or _condition._fields[i] == 'AND':
				print("Sous condition")
				if not isinstance(_condition[i], list):
					_str += " " + _condition._fields[i] + " ("
					_str += build_conditions(_condition[i])
					_str += ")"
				else:
					_str += build_conditions(_condition[i], _condition._fields[i])
			else:
				_str += _condition._fields[i] + " = "
				if isinstance(_condition[i], str):
					_str += _condition[i]
				else:
					_str += str(_condition[i])
	return _str
