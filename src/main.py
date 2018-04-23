import json
from collections import namedtuple
from flask import Flask
from flask import request
from src import *

app = Flask(__name__)


@app.route("/manoucheql", methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route("/manoucheql/<bdd>", methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route("/manoucheql/<bdd>/<table>", methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_all(bdd=None, table=None):
	if bdd is None or table is None:
		return "Euuuh, il manque un truc"

	o = json.loads(request.data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

	if request.method == 'GET':
		return "Récupération depuis " + bdd + "." + table
	elif request.method == 'POST':
		return condition.build_condition(o)
	return "T'es con"


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
