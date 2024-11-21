from random import randint, choice
from tests.mock import MOCK_CLUBS, MOCK_COMPETITIONS, MAX_PURCHASE


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
    club: dict = choose_club_with_points()
    competition: dict = choose_comp_with_points()
    max_usable_club_points: int = randint(1, min(MAX_PURCHASE, int(club["points"])))
    valid_places: int = min(int(competition["numberOfPlaces"]), max_usable_club_points)

    valid_booking_form: dict = {"club": club["name"],
                                "competition": competition["name"],
                                "places": valid_places}

    return club, competition, valid_places, valid_booking_form


def test_points_and_places_update(client, mock_clubs, mock_competitions) -> None:
    club, comp, places_number, booking_form = init_random_data()

    club_places_before: int = int(club["points"])
    comp_places_before: int = int(comp["numberOfPlaces"])
    response = client.post("/purchasePlaces", data=booking_form)

    assert response.status_code == 200

    club_places_after: int = int(club["points"])
    comp_places_after: int = int(comp["numberOfPlaces"])
    check_points_computation: bool = club_places_after == club_places_before - places_number
    check_places_computation: bool = comp_places_after == comp_places_before - places_number

    assert club_places_before > club_places_after and check_points_computation
    assert comp_places_before > comp_places_after and check_places_computation

    # reset data as we want correct data for the next units tests
    club["points"] = str(club_places_before)
    comp["numberOfPlaces"] = str(comp_places_before)
