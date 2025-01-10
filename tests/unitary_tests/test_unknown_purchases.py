from server import MAX_PLACES
from tests.mock import INVALID_CLUB, VALID_CLUB, INVALID_COMP, VALID_COMP, WELCOME_PAGE


def test_invalid_club_purchases(client, mock_clubs, mock_competitions) -> None:
    booking_form = {"club": INVALID_CLUB, "competition": VALID_COMP, "places": MAX_PLACES}
    response = client.post("/purchasePlaces", data=booking_form)
    assert response.status_code == 302
    assert not WELCOME_PAGE in response.data

def test_invalid_competition_purchases(client, mock_clubs, mock_competitions) -> None:
    booking_form = {"club": VALID_CLUB, "competition": INVALID_COMP, "places": MAX_PLACES}
    response = client.post("/purchasePlaces", data=booking_form)
    assert response.status_code == 302
    assert not WELCOME_PAGE in response.data