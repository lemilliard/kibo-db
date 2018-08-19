import requests
import json

from src.main.config import active_config

base_url = "http://localhost:" + str(active_config.port)
headers = {'Content-Type': 'application/json'}


def delete_database(database_name: str):
    path = "/admin/database/" + database_name
    response = requests.request("DELETE", base_url + path, headers=headers)
    return response.text


def create_database(database: dict):
    path = "/admin/database"
    response = requests.request("POST", base_url + path, json=database, headers=headers)
    return response.json()["system_name"]


def create_table(database_name: str, table: dict):
    path = "/admin/database/" + database_name + "/table"
    response = requests.request("POST", base_url + path, json=table, headers=headers)
    return response.text


def init():
    print(delete_database("system"))

    database = {"name": "System", "description": "System database"}
    database_name = create_database(database)

    table = {
        "name": "User",
        "description": "User table",
        "fields": [
            {
                "id": True,
                "name": "ID User",
                "type": "integer"
            },
            {
                "name": "Username",
                "type": "string"
            },
            {
                "name": "Password",
                "type": "password"
            }
        ]
    }
    print(create_table(database_name, table))


init()
