def load(path, schema):
    json = ""

    with open(path) as f:
        content = f.read()
        process_content(content)


def process_content(content):
    verif_content(content)

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
                    print(current_key, current_value)
                    if "{" in current_value:
                        process_content(current_value)
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


def verif_content(content):
    if content[0] not in ["{", "["]:
        raise Exception("Le premier caractère est invalide")
    elif content[len(content) - 1] not in ["}", "]"]:
        raise Exception("Le dernier caractère est invalide")


def get_value_type(char):
    if char == "\"":
        return "str"
    elif char == "[":
        return "arr"
    elif char == "{":
        return "obj"
    else:
        return "num"


schema = "{id_user,first_name}"

load("../../../../databases/test/user/data/1.json", schema)
