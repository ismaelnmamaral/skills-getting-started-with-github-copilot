import copy

import pytest
from fastapi.testclient import TestClient

from app import app, activities


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    # Deep copy/restore so signup/unregister tests don't leak state across tests
    original = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(original)
