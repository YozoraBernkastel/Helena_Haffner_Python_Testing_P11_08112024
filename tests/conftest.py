import pytest
import server
from tests.mock import MOCK_CLUBS, MOCK_COMPETITIONS

@pytest.fixture
def client():
    server.app.config.update({"TESTING": True})

    with server.app.test_client() as client:
        yield client


@pytest.fixture
def mock_clubs():
    server.clubs = MOCK_CLUBS

@pytest.fixture
def mock_competitions():
    server.past_competition_places_filter(MOCK_COMPETITIONS)
    server.competitions = MOCK_COMPETITIONS
