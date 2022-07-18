class Err(Exception):
    pass

class ClientError(Err):
    def __init__(self, status_code, error_message, header):
        # response status code
        self.status_code = status_code
        # error message returned from API
        self.error_message = error_message
        # the whole response header returned from API
        self.header = header

class ServerError(Err):
    def __init__(self, status_code, message):
        # response status code
        self.status_code = status_code
        # error message returned from API
        self.message = message

class InsufficientBalance(Err):
    def __init__(self, status_code, message):
        # response status code
        self.status_code = status_code
        # error message returned from API
        self.error_message = message