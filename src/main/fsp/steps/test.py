import re

# string = "{sous_objet: {id1, liste_objets: {id2, test}, sous_objet: {id3}}}"
string = "{id1, liste_objets: {id2, test: {id5}}, sous_objet: {id3}}"

# search = re.search("{.*}", string[1:-1])
# if search is not None:
#     print(search.group())

cpt = 0
tmp = ""
test = False

i = 1
while i in range(1, string.__len__() - 1):
    c = string[i]
    if c == "{":
        test = True
        cpt += 1
    elif c == "}":
        cpt -= 1
    if test:
        tmp += c
        if cpt == 0:
            print(tmp)
            test = False
            i = string.__len__()
    i += 1