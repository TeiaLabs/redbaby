class RedBabyError(Exception):
    pass


class ClientNotFoundError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(f"Redbaby Client not found: {self.message}")


class ConnectionNotFoundError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(f"Redbaby Connection not found: {self.message}")
