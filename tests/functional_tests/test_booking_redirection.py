from tests.data_helper import booking_page
from tests.conftest import mock_clubs, mock_competitions
from tests.mock import (VALID_COMP, INVALID_COMP, THIRTEEN_POINTS_CLUB, INVALID_CLUB,
                        WELCOME_PAGE, FUTURE_THIRTY_SEVEN_PLACES_COMP)


def test_valid_redirection(client, mock_clubs, mock_competitions):
    comp_name = FUTURE_THIRTY_SEVEN_PLACES_COMP["name"]
    club_name = THIRTEEN_POINTS_CLUB["name"]

    response = client.get(f"/book/{comp_name}/{club_name}")
    assert response.status_code == 200
    assert booking_page(comp_name) in response.data

def test_unknown_club_redirection(client, mock_clubs, mock_competitions):
    comp_name = VALID_COMP
    club_name = INVALID_CLUB

    response = client.get(f"/book/{comp_name}/{club_name}")
    assert response.status_code == 302
    assert not booking_page(comp_name) in response.data

def test_unknown_comp_redirection(client, mock_clubs, mock_competitions):
    comp_name = INVALID_COMP
    club_name = THIRTEEN_POINTS_CLUB["name"]

    response = client.get(f"/book/{comp_name}/{club_name}")
    assert response.status_code == 200
    assert not booking_page(comp_name) in response.data
    assert WELCOME_PAGE in response.data
