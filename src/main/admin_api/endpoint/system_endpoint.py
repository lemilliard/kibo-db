from src.main.common.model import endpoint


class SystemEndpoint(endpoint.Endpoint):

    @staticmethod
    def connect():
        _response = None
        _body = SystemEndpoint.get_body()
        _username = _body.get("username", None)
        _password = _body.get("password", None)
        if _username is not None and _password is not None:
            _response = True
        return _response
