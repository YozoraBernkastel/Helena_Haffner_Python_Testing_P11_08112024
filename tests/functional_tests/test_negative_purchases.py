from tests.data_helper import html_club_points, valid_data
from tests.mock import NO_PURCHASE_MESSAGE


def init_data() -> tuple[dict, dict, int, dict]:
    club, competition = valid_data()
    negative_places: int = -10

    too_many_purchases_form: dict = {"club": club["name"],
                                     "competition": competition["name"],
                                     "places": negative_places}

    return club, competition, negative_places, too_many_purchases_form


def test_negative_purchase(client) -> None:
    club, comp, negatives_places, booking_form = init_data()
    assert negatives_places < 0

    club_points_before: int = int(club["points"])
    comp_places_before: int = int(comp["numberOfPlaces"])
    response = client.post("/purchasePlaces", data=booking_form)

    assert response.status_code == 200
    assert html_club_points(club_points_before) in response.data
    assert NO_PURCHASE_MESSAGE in response.data

    club_points_after: int = int(club["points"])
    comp_places_after: int = int(comp["numberOfPlaces"])

    assert club_points_before == club_points_after
    assert comp_places_before == comp_places_after
