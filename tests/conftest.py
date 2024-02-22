import pytest

from redbaby.database import DB


@pytest.fixture(scope="session", autouse=True)
def start_db():
    DB.add_client()
