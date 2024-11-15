from random import randint, choice
from tests.mock import MOCK_CLUBS, MOCK_COMPETITIONS


def choose_club_with_points() -> dict:
    clubs: list = [club for club in MOCK_CLUBS if int(club["points"]) > 0]

    if len(clubs) > 0:
        return choice(clubs)

    raise Exception("There is no clubs with points")


def choose_comp_with_points() -> dict:
    comps: list = [comp for comp in MOCK_COMPETITIONS if int(comp["numberOfPlaces"]) > 0]

    if len(comps) > 0:
        return choice(comps)

    raise Exception("There is no competition with remain places")


def init_random_data() -> tuple[dict, dict, int, dict]:
    club = choose_club_with_points()
    competition = choose_comp_with_points()
    max_usable_club_points = randint(1, min(12, int(club["points"])))
    valid_places = min(int(competition["numberOfPlaces"]), max_usable_club_points)

    valid_booking_form: dict = {"club": club["name"],
                                "competition": competition["name"],
                                "places": valid_places}

    return club, competition, valid_places, valid_booking_form


def test_user_points_are_removed(client, mock_clubs, mock_competitions):
    club, comp, places_number, booking_form = init_random_data()

    club_places_before: int = int(club["points"])
    response = client.post("/purchasePlaces", data=booking_form)

    assert response.status_code == 200

    club_places_after: int = int(club["points"])
    check_computation: bool = club_places_after == club_places_before - places_number

    assert club_places_before > club_places_after and check_computation


def test_competition_number_of_places_decrease(client):
    club, comp, places_number, booking_form = init_random_data()

    club_places_before: int = int(comp["numberOfPlaces"])
    response = client.post("/purchasePlaces", data=booking_form)

    assert response.status_code == 200

    club_places_after: int = int(comp["numberOfPlaces"])
    check_computation: bool = club_places_after == club_places_before - places_number

    assert club_places_before > club_places_after and check_computation
