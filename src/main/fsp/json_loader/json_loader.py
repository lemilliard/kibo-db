def load(path, schema):
    json = ""

    with open(path) as f:
        content = f.read()
        json += process_content(content, schema)

    return json


def process_content(content, schema):
    import re

    (open_tag, close_tag) = verif_content(content)

    json = open_tag

    key_opened = False
    value_opened = False
    current_key = ""
    current_value = ""
    waiting_value = False

    value_type = None

    is_escaped = False

    count_arrays = 0
    count_objects = 0

    for c in content:
        if key_opened:
            if c == "\"":
                key_opened = False
            else:
                current_key += c
        elif value_opened:
            if c == "[" and value_type in [None, "arr"]:
                count_arrays += 1
            elif c == "{" and value_type in [None, "obj"]:
                count_objects += 1

            is_closing_string = (c == "\"" and value_type == "str")
            is_closing_array = (c == "]" and value_type == "arr")
            is_closing_object = (c == "}" and value_type == "obj")
            is_closing_number = (c in [",", "\n", "\r\n", "}", "]"] and value_type == "num")

            if not is_closing_number:
                current_value += c

            if is_closing_string \
                    or is_closing_array \
                    or is_closing_object \
                    or is_closing_number:
                if is_escaped:
                    is_escaped = False
                elif is_closing_array and count_arrays > 0:
                    count_arrays -= 1
                elif is_closing_object and count_objects > 0:
                    count_objects -= 1
                else:
                    if is_key_valid(current_key, schema):
                        if "{" in current_value:
                            sous_schema = re.search("{(.*)}", schema[1:-1])
                            if sous_schema is not None:
                                json += "\"" + current_key + "\":"
                                sous_schema = sous_schema.group()
                                if value_type == "arr":
                                    json += "["
                                    for sub_value in re.findall("{(.*)}", current_value):
                                        sub_value = "{" + sub_value + "}"
                                        json += process_content(sub_value, sous_schema) + ","
                                    json = json[:-1]
                                    json += "]"
                                else:
                                    json += process_content(current_value, sous_schema)
                                json += ","
                        else:
                            json += "\"" + current_key + "\":" + current_value + ","
                    value_opened = False
                    current_key = ""
            elif value_type == "str" and c == "\\":
                is_escaped = True
        elif waiting_value:
            if c not in [" ", "\n", "\r\n"]:
                value_type = get_value_type(c)
                current_value = c
                value_opened = True
                waiting_value = False
        else:
            if c == "\"" and current_key == "":
                key_opened = True
            elif c == ":":
                value_type = None
                waiting_value = True
    if json.endswith(","):
        json = json[:-1]
    json += close_tag
    return json


def is_key_valid(key, schema):
    import re
    s = schema.replace(" ", "")
    if s.startswith("{"):
        s = s[1:]
    if s.endswith("}"):
        s = s[:-1]
    s = re.sub("{(.*)}", "", s)
    return s.__contains__(key)


def verif_content(content):
    if content[0] not in ["{", "["]:
        raise Exception("Le premier caractère est invalide")
    elif content[len(content) - 1] not in ["}", "]"]:
        raise Exception("Le dernier caractère est invalide")
    else:
        return content[0], content[len(content) - 1]


def get_value_type(char):
    if char == "\"":
        return "str"
    elif char == "[":
        return "arr"
    elif char == "{":
        return "obj"
    else:
        return "num"
