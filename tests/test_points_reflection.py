from tests.mock import VALID_POINTS_BOOKING, CLUB, VALID_PLACES, COMPETITION


def test_user_points_are_removed(client, mock_clubs, mock_competitions):
    club_places_before: int = int(CLUB["points"])
    response = client.post("/purchasePlaces", data=VALID_POINTS_BOOKING)

    assert response.status_code == 200

    club_places_after: int = int(CLUB["points"])
    check_computation: bool = club_places_after == club_places_before - VALID_PLACES

    assert club_places_before > club_places_after and check_computation


def test_competition_number_of_places_decrease(client):
    club_places_before: int = int(COMPETITION["numberOfPlaces"])
    response = client.post("/purchasePlaces", data=VALID_POINTS_BOOKING)

    assert response.status_code == 200

    club_places_after: int = int(COMPETITION["numberOfPlaces"])
    check_computation: bool = club_places_after == club_places_before - VALID_PLACES

    assert club_places_before > club_places_after and check_computation
