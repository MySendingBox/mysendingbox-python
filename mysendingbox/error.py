from __future__ import unicode_literals


class MysendingboxError(Exception):

    def __init__(self, message=None, http_body=None, http_status=None,
                 json_body=None):
        super(MysendingboxError, self).__init__(message)
        self.http_body = http_body
        self.http_status = http_status
        self.json_body = json_body


class APIError(MysendingboxError):
    pass


class APIConnectionError(MysendingboxError):
    pass


class AuthenticationError(MysendingboxError):
    pass


class InvalidRequestError(MysendingboxError):
    pass
