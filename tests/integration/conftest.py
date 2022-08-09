import pytest
from fastapi.testclient import TestClient

from main import init_app


@pytest.fixture
def app():
    yield init_app()


@pytest.fixture
def api_client(app):
    return TestClient(app)
