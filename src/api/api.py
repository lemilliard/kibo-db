import json
from collections import namedtuple

from flask import request
from src.api.condition import *


def api_endpoint(p_bdd=None, p_table=None):
    bdd = get_bdd(p_bdd)
    table = get_table(p_table)
    if request.method == 'GET':
        return do_get(bdd, table)
    elif request.method == 'POST':
        return do_post(bdd, table)
    elif request.method == 'PUT':
        return do_put(bdd, table)
    elif request.method == 'DELETE':
        return do_delete(bdd, table)
    return "T'es con"


def do_get(bdd, table):
    print("GET: " + bdd + "." + table)
    return "OK"


def do_post(bdd, table):
    print("POST: " + bdd + "." + table)
    body = get_body()
    if body:
        return condition.build_condition(body)
    return "Manque le body"


def do_put(bdd, table):
    print("PUT: " + bdd + "." + table)
    return "OK"


def do_delete(bdd, table):
    print("DELETE: " + bdd + "." + table)
    return "OK"


def get_body():
    if request.json is None:
        return False
    return json.loads(request.data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))


def get_bdd(bdd=None):
    if bdd is None:
        return ""
    return bdd


def get_table(table=None):
    if table is None:
        return ""
    return table
