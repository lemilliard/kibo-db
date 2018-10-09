def update_indexes(file):
    pass


def delete_indexes(file):
    pass

def find_index_file(cond, path):
    import os
    function_operator = equal_operator
    operator = cond["operator"]
    if operator == ">":
        function_operator = superior_operator
    elif operator == "<":
        function_operator = inferior_operator
    elif operator == "<=":
        function_operator = inferior_or_equal_operator
    elif operator == ">=":
        function_operator = superior_or_equal_operator
    file_list = os.listdir(path)
    for file in file_list:
        part_name = file.split('-')
        if file.endswith('.json'):
            if function_operator(part_name, cond["value"]):
                yield file
        else:
            if function_operator(part_name, cond["value"]):
                yield from find_index_file(cond, path + "/" + file)

def equal_operator(part_name, cond_value):
    if len(part_name) > 1 and part_name[0] < cond_value < part_name[1]:
        return True
    return False

def superior_operator(part_name, cond_value):
    if len(part_name) > 1 and part_name[1] > cond_value:
        return True
    return False

def inferior_operator(part_name, cond_value):
    if len(part_name) > 1 and part_name[0] < cond_value:
        return True
    return False

def superior_or_equal_operator(part_name, cond_value):
    if equal_operator(part_name, cond_value):
        return True
    elif superior_operator(part_name, cond_value):
        return True
    return False

def inferior_or_equal_operator(part_name, cond_value):
    if equal_operator(part_name, cond_value):
        return True
    elif inferior_operator(part_name, cond_value):
        return True
    return False

params = {
    "path": "../../../../databases",
    "value": "brioche",
    "operator": ">"
}
result = find_index_file(params, "../../../../databases")
for i in result:
    print(i)