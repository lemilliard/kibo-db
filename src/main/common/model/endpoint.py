class Endpoint(object):

    @staticmethod
    def get_body() -> dict:
        from flask import request
        if request.json is None:
            return False
        return request.json

    @classmethod
    def process_request(cls, *args, **kwargs):
        from flask import request
        response = "T'es con"
        if request.method == "GET":
            response = cls.do_get(*args, **kwargs)
        elif request.method == "POST":
            response = cls.do_post(*args, **kwargs)
        elif request.method == "PUT":
            response = cls.do_put(*args, **kwargs)
        elif request.method == "DELETE":
            response = cls.do_delete(*args, **kwargs)
        return response

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
