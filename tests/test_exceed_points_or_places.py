from server import MAX_PLACES
from tests.mock import MAX_PURCHASE
from tests.choice_data_helper import (choose_club_with_less_than_twelve_points,
                                      choose_comp_with_more_than_twelve_points,
                                      choose_club_with_more_than_twelve_points,
                                      choose_comp_with_less_than_twelve_points)


def init_random_data_exceeds_club_points() -> tuple[dict, dict, int, dict]:
    club: dict = choose_club_with_less_than_twelve_points()
    competition: dict = choose_comp_with_more_than_twelve_points()

    more_purchase_than_point = int(club["points"]) + 1
    too_many_purchases_form: dict = {"club": club["name"],
                                     "competition": competition["name"],
                                     "places": more_purchase_than_point}

    return club, competition, more_purchase_than_point, too_many_purchases_form


def test_exceeds_club_points(client) -> None:
    club, comp, purchases, booking_form = init_random_data_exceeds_club_points()
    assert purchases <= MAX_PURCHASE
    assert purchases > int(club["points"])

    club_places_before: int = int(club["points"])
    comp_places_before: int = int(comp["numberOfPlaces"])
    response = client.post("/purchasePlaces", data=booking_form)

    assert response.status_code == 200
    club_places_after: int = int(club["points"])
    comp_places_after: int = int(comp["numberOfPlaces"])

    assert club_places_before == club_places_after
    assert comp_places_before == comp_places_after


def init_random_data_exceeds_comp_places() -> tuple[dict, dict, int, dict]:
    club: dict = choose_club_with_more_than_twelve_points()
    competition: dict = choose_comp_with_less_than_twelve_points()

    too_many_purchases_form: dict = {"club": club["name"],
                                     "competition": competition["name"],
                                     "places": MAX_PLACES}

    return club, competition, MAX_PLACES, too_many_purchases_form

def test_exceeds_competition_places(client) -> None:
    club, comp, purchases, booking_form = init_random_data_exceeds_comp_places()
    assert purchases > int(comp["numberOfPlaces"])

    club_places_before: int = int(club["points"])
    comp_places_before: int = int(comp["numberOfPlaces"])
    response = client.post("/purchasePlaces", data=booking_form)

    assert response.status_code == 200
    club_places_after: int = int(club["points"])
    comp_places_after: int = int(comp["numberOfPlaces"])

    assert club_places_before == club_places_after
    assert comp_places_before == comp_places_after
