from tests.mock import VALID_CONNECTION, THIRTEEN_POINTS_CLUB, INVALID_CONNECTION, INDEX_PAGE, WELCOME_PAGE
from tests.data_helper import welcome_club


def test_homepage(client, mock_clubs, mock_competitions):
    response = client.get("/")
    assert response.status_code == 200
    assert INDEX_PAGE in response.data


def test_connexion_with_existing_mail(client, mock_clubs, mock_competitions):
    response = client.post("/showSummary", data=VALID_CONNECTION)
    assert response.status_code == 200
    assert WELCOME_PAGE in response.data
    assert welcome_club(THIRTEEN_POINTS_CLUB["name"])


def test_connexion_with_unknown_mail(client, mock_clubs, mock_competitions):
    response = client.post("/showSummary", data=INVALID_CONNECTION)
    assert response.status_code == 200
    assert not WELCOME_PAGE in response.data
    assert INDEX_PAGE in response.data

