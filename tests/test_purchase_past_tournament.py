from server import is_competition_in_past
from tests.choice_data_helper import choose_club_with_points, choose_random_past_competition
from tests.mock import valid_places_purchase


def init_random_data() -> tuple[dict, dict, int, dict]:
    club = choose_club_with_points()
    competition = choose_random_past_competition()
    purchased_places = valid_places_purchase(club, competition)

    valid_booking_form: dict = {"club": club["name"],
                                "competition": competition["name"],
                                "places": purchased_places}

    return club, competition, purchased_places, valid_booking_form


def test_past_competition_behavior(client) -> None:
    club, comp, purchased_places, booking_form = init_random_data()

    assert is_competition_in_past(comp["date"])
    assert purchased_places == 0

    club_places_before: int = int(club["points"])
    comp_places_before: int = int(comp["numberOfPlaces"])
    response = client.post("/purchasePlaces", data=booking_form)

    assert response.status_code == 200
    assert b"the competition is already done" in response.data
    club_places_after: int = int(club["points"])
    comp_places_after: int = int(comp["numberOfPlaces"])

    assert club_places_before == club_places_after
    assert comp_places_before == comp_places_after

