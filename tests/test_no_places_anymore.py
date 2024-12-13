from server import comp_still_has_available_places, MAX_PLACES
from tests.mock import (FUTURE_THIRTY_SEVEN_PLACES_COMP, FUTURE_ZERO_PLACE_COMP, THIRTEEN_POINTS_CLUB,
                        NO_PLACE_ANYMORE_MESSAGE)

def test_comp_still_has_available_places():
    has_places = comp_still_has_available_places(FUTURE_THIRTY_SEVEN_PLACES_COMP)
    assert has_places

def test_comp_has_no_available_places():
    has_places = comp_still_has_available_places(FUTURE_ZERO_PLACE_COMP)
    assert not has_places

def init_data() -> tuple[dict, dict, int, dict]:
    club = THIRTEEN_POINTS_CLUB
    competition = FUTURE_ZERO_PLACE_COMP

    too_many_purchases_form: dict = {"club": club["name"],
                                     "competition": competition["name"],
                                     "places": MAX_PLACES}

    return club, competition, MAX_PLACES, too_many_purchases_form


def test_last_places_take_before_user_reservation(client) -> None:
    club, comp, too_many_places, booking_form = init_data()
    assert too_many_places > 0

    club_points_before: int = int(club["points"])
    comp_places_before: int = int(comp["numberOfPlaces"])
    response = client.post("/purchasePlaces", data=booking_form)

    assert response.status_code == 200
    club_points_after: int = int(club["points"])
    comp_places_after: int = int(comp["numberOfPlaces"])

    assert NO_PLACE_ANYMORE_MESSAGE in response.data
    assert club_points_before == club_points_after
    assert comp_places_before == comp_places_after