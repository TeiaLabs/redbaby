from pymongo.errors import PyMongoError


class RedBabyError(PyMongoError):
    """
    Generic error.
    """


class DocumentNotFound(RedBabyError):
    """
    Raised when no document is found.
    """


class ClientNotFoundError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(f"Redbaby Client not found: {self.message}")


class ConnectionNotFoundError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(f"Redbaby Connection not found: {self.message}")
