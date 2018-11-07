import re

# string = "{sous_objet: {id1, liste_objets: {id2, test}, sous_objet: {id3}}}"
string = "{id1, liste_objets: {id2, test: {id5}}, sous_objet: {id3}}"


# search = re.search("{.*}", string[1:-1])
# if search is not None:
#     print(search.group())


def get_sous_schema(schema):
    cpt = 0
    sous_schema = ""
    in_object = False
    i = 1
    while i in range(1, schema.__len__() - 1):
        c = schema[i]
        if c == "{":
            in_object = True
            cpt += 1
        elif c == "}":
            cpt -= 1
        if in_object:
            sous_schema += c
            if cpt == 0:
                i = schema.__len__()
        i += 1
    return sous_schema


print(get_sous_schema(string))
