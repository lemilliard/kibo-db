from flask import request


class Endpoint(object):

    @staticmethod
    def get_body() -> dict:
        if request.json is None:
            return False
        return request.json

    @classmethod
    def process_request(cls, *args, **kwargs):
        _response = "T'es con"
        if request.method == "GET":
            _response = cls.do_get(*args, **kwargs)
        elif request.method == "POST":
            _response = cls.do_post(*args, **kwargs)
        elif request.method == "PUT":
            _response = cls.do_put(*args, **kwargs)
        elif request.method == "DELETE":
            _response = cls.do_delete(*args, **kwargs)
        return _response

    @classmethod
    def do_get(cls, *args, **kwargs):
        return None

    @classmethod
    def do_post(cls, *args, **kwargs):
        return None

    @classmethod
    def do_put(cls, *args, **kwargs):
        return None

    @classmethod
    def do_delete(cls, *args, **kwargs):
        return None
