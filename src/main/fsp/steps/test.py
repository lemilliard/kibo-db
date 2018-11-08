import re
import queue
import time
import threading
# string = "{sous_objet: {id1, liste_objets: {id2, test}, sous_objet: {id3}}}"
string = "{id1, liste_objets: {id2, test: {id5}}, sous_objet: {id3, sous_objet: {id4}}}"


# search = re.search("{.*}", string[1:-1])
# if search is not None:
#     print(search.group())

# def get_sous_schema(schema, key):
#     cpt = 0
#     tmp_sous_schema = ""
#     sous_schema = ""
#     in_object = False
#     in_key = False
#     tmp_key = ""
#     for c in string[1:-1]:
#         if c == "{":
#             in_object = True
#             cpt += 1
#         elif c == "}":
#             cpt -= 1
#         if in_object:
#             tmp_sous_schema += c
#             if cpt == 0:
#                 if key == tmp_key:
#                     sous_schema = tmp_sous_schema
#                 in_object = False
#                 in_key = False
#                 tmp_sous_schema = ""
#                 tmp_key = ""
#         else:
#             if c in [",", " "] and not in_key:
#                 tmp_key = ""
#             else:
#                 if c == ":":
#                     in_key = True
#                 if not in_key:
#                     tmp_key += c
#     return sous_schema

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

# def get_sous_schema(schema):
#     cpt = 0
#     sous_schema = ""
#     in_object = False
#     i = 1
#     while i in range(1, schema.__len__() - 1):
#         c = schema[i]
#         if c == "{":
#             in_object = True
#             cpt += 1
#         elif c == "}":
#             cpt -= 1
#         if in_object:
#             sous_schema += c
#             if cpt == 0:
#                 i = schema.__len__()
#         i += 1
#     return sous_schema
#
#
# print(get_sous_schema(string))

def is_key_valid(key, s):
    return s.__contains__(key)

q = queue.Queue()
def feed_queue():
    global q
    q.put(0)
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    for i in range(5, 10):
        time.sleep(1)
        print("sleep")
        q.put(i)
    q.put(None)

def consume_queue():
    global q
    c = q.get()
    while c is not None:
        print(c)
        c = q.get()

# s = get_sous_schema(string, "liste_objets")
# print(s)
# s = get_sous_schema(string, "sous_objet")
# print(s)
#
# print(is_key_valid("sous_objet", s[1]))


threads = []
for func in [feed_queue, consume_queue]:
    threads.append(threading.Thread(target=func))
    threads[-1].start()

for thread in threads:
    thread.join()
