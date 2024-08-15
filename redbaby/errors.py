from typing import Iterable

from pymongo.errors import PyMongoError


class RedBabyError(PyMongoError):
    """
    Generic error.
    """

    def __init__(
        self,
        message: str = "",
        error_labels: Iterable[str] | None = None,
    ) -> None:
        if not message:
            message = "An unknown error occurred."
        super().__init__(message, error_labels)


class DocumentNotFound(RedBabyError):
    """
    Raised when no document is found.
    """

    def __init__(
        self,
        message: str = "",
        error_labels: Iterable[str] | None = None,
    ) -> None:
        if not message:
            message = "Document not found."
        super().__init__(message, error_labels)


class InvalidUpdateDict(RedBabyError):
    """
    Raised when an invalid update dictionary is passed to a method.
    """

    def __init__(
        self,
        message: str = "",
        error_labels: Iterable[str] | None = None,
    ) -> None:
        if not message:
            message = "Invalid update dictionary."
        super().__init__(message, error_labels)
