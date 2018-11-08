def load_with_schema(**args):
    path = args.get("path")
    schema = args.get("schema")

    json = ""

    with open(path) as f:
        content = f.read()
        json += process_content(content, schema)

    return json


def load(**args):
    path = args.get("path")
    with open(path) as f:
        json = f.read()
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
                    (sous_schema, keys) = get_sous_schema(schema, current_key)
                    if keys.__contains__(current_key):
                        if "{" in current_value:
                            json += "\"" + current_key + "\":"
                            if value_type == "arr":
                                json += "["
                                for sub_value in re.findall("{(.*?)}", current_value):
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
    return schema.__contains__(key)


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


def get_sous_schema(schema, key):
    cpt = 0
    tmp_sous_schema = ""
    sous_schema = ""
    in_object = False
    in_key = False
    tmp_key = ""
    i = 1
    keys = []
    while i in range(1, schema.__len__()):
        c = schema[i]
        if c == "{":
            in_object = True
            cpt += 1
        elif c == "}":
            cpt -= 1
        if in_object:
            tmp_sous_schema += c
            if cpt == 0:
                if key == tmp_key:
                    sous_schema = tmp_sous_schema

                keys.append(tmp_key)
                in_object = False
                in_key = False
                tmp_sous_schema = ""
                tmp_key = ""
        else:
            if (c in [",", " "] or i == schema.__len__() - 1) and not in_key:
                if not in_object and tmp_key != "":
                    keys.append(tmp_key)
                tmp_key = ""
            else:
                if c == ":":
                    in_key = True
                if not in_key:
                    tmp_key += c
        i += 1
    return sous_schema, keys
