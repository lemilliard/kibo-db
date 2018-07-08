from flask import request


class Endpoint(object):

    @staticmethod
    def get_body() -> dict:
        if request.json is None:
            return False
        return request.json
