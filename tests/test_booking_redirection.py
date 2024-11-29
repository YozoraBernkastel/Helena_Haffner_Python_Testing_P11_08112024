from tests.data_helper import init_valid_comp_club
from tests.conftest import mock_clubs, mock_competitions
from tests.mock import VALID_COMP, INVALID_COMP, VALID_CLUB, INVALID_CLUB, booking_page, INDEX_PAGE, WELCOME_PAGE


def test_valid_redirection(client, mock_clubs, mock_competitions):
    comp_name, club_name = init_valid_comp_club()

    response = client.get(f"/book/{comp_name}/{club_name}")
    assert response.status_code == 200
    assert booking_page(comp_name) in response.data

def test_unknown_club_redirection(client, mock_clubs, mock_competitions):
    comp_name = VALID_COMP
    club_name = INVALID_CLUB

    response = client.get(f"/book/{comp_name}/{club_name}")
    assert response.status_code == 200
    assert not booking_page(comp_name) in response.data
    assert INDEX_PAGE in response.data

def test_unknown_comp_redirection(client, mock_clubs, mock_competitions):
    comp_name = INVALID_COMP
    club_name = VALID_CLUB

    response = client.get(f"/book/{comp_name}/{club_name}")
    assert response.status_code == 200
    assert not booking_page(comp_name) in response.data
    assert WELCOME_PAGE in response.data
