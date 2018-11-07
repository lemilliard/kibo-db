import re

#string = "{sous_objet: {id1, liste_objets: {id2, test}, sous_objet: {id3}}}"
string = "{id1, liste_objets: {id2, test: {id5}}, sous_objet: {id3}}"

search = re.search("{.*}", string[1:-1])
if search is not None:
    print(search.group())
