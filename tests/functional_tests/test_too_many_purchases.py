from server import MAX_PLACES
from tests.data_helper import valid_data


def init_data() -> tuple[dict, dict, int, dict]:
    club, competition = valid_data()
    too_many_places: int = MAX_PLACES + 1

    too_many_purchases_form: dict = {"club": club["name"],
                                     "competition": competition["name"],
                                     "places": too_many_places}

    return club, competition, too_many_places, too_many_purchases_form


def test_too_many_purchase(client) -> None:
    club, comp, too_many_places, booking_form = init_data()
    assert too_many_places > MAX_PLACES

    club_points_before: int = int(club["points"])
    comp_places_before: int = int(comp["numberOfPlaces"])
    response = client.post("/purchasePlaces", data=booking_form)

    assert response.status_code == 200
    club_points_after: int = int(club["points"])
    comp_places_after: int = int(comp["numberOfPlaces"])

    assert club_points_before == club_points_after
    assert comp_places_before == comp_places_after

