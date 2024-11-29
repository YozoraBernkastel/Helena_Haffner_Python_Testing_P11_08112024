from server import MAX_PLACES
from tests.data_helper import html_club_points
from tests.mock import FOUR_POINTS_CLUB, THIRTY_SEVEN_PLACES_COMP, WELCOME_PAGE, THIRTEEN_POINTS_CLUB, \
    TWO_PLACES_COMP, NO_PURCHASE_MESSAGE


def init_data_exceeds_club_points() -> tuple[dict, dict, int, dict]:
    club: dict = FOUR_POINTS_CLUB
    competition: dict = THIRTY_SEVEN_PLACES_COMP

    too_many_purchases_form: dict = {"club": club["name"],
                                     "competition": competition["name"],
                                     "places": MAX_PLACES}

    return club, competition, MAX_PLACES, too_many_purchases_form


def test_exceeds_club_points(client) -> None:
    club, comp, purchases, booking_form = init_data_exceeds_club_points()
    assert purchases <= MAX_PLACES
    assert purchases > int(club["points"])

    club_points_before: int = int(club["points"])
    comp_places_before: int = int(comp["numberOfPlaces"])
    response = client.post("/purchasePlaces", data=booking_form)

    assert response.status_code == 200
    assert WELCOME_PAGE in response.data
    assert html_club_points(club_points_before) in response.data
    assert NO_PURCHASE_MESSAGE in response.data

    club_points_after: int = int(club["points"])
    comp_places_after: int = int(comp["numberOfPlaces"])

    assert club_points_before == club_points_after
    assert comp_places_before == comp_places_after


def init_data_exceeds_comp_places() -> tuple[dict, dict, int, dict]:
    club: dict = THIRTEEN_POINTS_CLUB
    competition: dict = TWO_PLACES_COMP

    too_many_purchases_form: dict = {"club": club["name"],
                                     "competition": competition["name"],
                                     "places": MAX_PLACES}

    return club, competition, MAX_PLACES, too_many_purchases_form


def test_exceeds_competition_places(client) -> None:
    club, comp, purchases, booking_form = init_data_exceeds_comp_places()
    assert purchases > int(comp["numberOfPlaces"])

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
