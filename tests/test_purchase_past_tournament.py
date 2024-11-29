from server import is_competition_in_past, MAX_PLACES
from tests.mock import THIRTEEN_POINTS_CLUB, PAST_COMP


def init_random_data() -> tuple[dict, dict, int, dict]:
    club = THIRTEEN_POINTS_CLUB
    competition = PAST_COMP
    purchased_places = MAX_PLACES

    valid_booking_form: dict = {"club": club["name"],
                                "competition": competition["name"],
                                "places": purchased_places}

    return club, competition, purchased_places, valid_booking_form


def test_past_competition_behavior(client) -> None:
    club, comp, purchased_places, booking_form = init_random_data()

    assert is_competition_in_past(comp["date"])
    assert comp["numberOfPlaces"] == 0

    club_points_before: int = int(club["points"])
    comp_places_before: int = int(comp["numberOfPlaces"])
    response = client.post("/purchasePlaces", data=booking_form)

    assert response.status_code == 200
    assert b"the competition is already done" in response.data

    club_points_after: int = int(club["points"])
    comp_places_after: int = int(comp["numberOfPlaces"])

    assert club_points_before == club_points_after
    assert comp_places_before == comp_places_after

