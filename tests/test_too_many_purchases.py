from random import randint, choice
from tests.mock import MOCK_CLUBS, MOCK_COMPETITIONS, MAX_PURCHASE


def choose_club_with_more_than_twelve_points() -> dict:
    clubs: list = [club for club in MOCK_CLUBS if int(club["points"]) > MAX_PURCHASE]

    if len(clubs) > 0:
        return choice(clubs)

    raise Exception("There is no clubs with more than 12 points")


def choose_comp_with_more_than_twelve_points() -> dict:
    comps: list = [comp for comp in MOCK_COMPETITIONS if int(comp["numberOfPlaces"]) > MAX_PURCHASE]

    if len(comps) > 0:
        return choice(comps)

    raise Exception("There is no competition with more than 12 remain places")


def max_available_purchase(club_points: str, comp_places: str) -> int:
    club_points = int(club_points)
    comp_places = int(comp_places)
    max_available_places: int = club_points if comp_places > club_points else comp_places

    return randint(MAX_PURCHASE + 1, max_available_places)


def init_random_data() -> tuple[dict, dict, int, dict]:
    club: dict = choose_club_with_more_than_twelve_points()
    competition: dict = choose_comp_with_more_than_twelve_points()

    too_many_places: int = max_available_purchase(club["points"], competition["numberOfPlaces"])

    too_many_purchases_form: dict = {"club": club["name"],
                                     "competition": competition["name"],
                                     "places": too_many_places}

    return club, competition, too_many_places, too_many_purchases_form


def test_too_many_purchase(client) -> None:
    club, comp, too_many_places, booking_form = init_random_data()
    assert too_many_places > MAX_PURCHASE

    club_places_before: int = int(club["points"])
    comp_places_before: int = int(comp["numberOfPlaces"])
    response = client.post("/purchasePlaces", data=booking_form)

    assert response.status_code == 200
    club_places_after: int = int(club["points"])
    comp_places_after: int = int(comp["numberOfPlaces"])

    assert club_places_before == club_places_after
    assert comp_places_before == comp_places_after

