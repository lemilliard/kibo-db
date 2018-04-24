from flask import Flask
from src.api import api
from src.client import client

app = Flask(__name__, template_folder="client/view")
app.config['DEBUG'] = True


@app.route('/api', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/api/<bdd>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/api/<bdd>/<table>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_endpoint(p_bdd=None, p_table=None):
    return api.api_endpoint(p_bdd, p_table)


@app.route('/client')
@app.route('/client/<path:page>')
def client_endpoint(page=None):
    return client.client_endpoint(page)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
