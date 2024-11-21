from random import randint
from tests.choice_data_helper import choose_random_club, choose_random_competition


def init_random_data() -> tuple[dict, dict, int, dict]:
    club: dict = choose_random_club()
    competition: dict = choose_random_competition()

    negative_places: int = randint(-12, -1)

    too_many_purchases_form: dict = {"club": club["name"],
                                     "competition": competition["name"],
                                     "places": negative_places}

    return club, competition, negative_places, too_many_purchases_form


def test_negative_purchase(client) -> None:
    club, comp, negatives_places, booking_form = init_random_data()
    assert negatives_places < 0

    club_places_before: int = int(club["points"])
    comp_places_before: int = int(comp["numberOfPlaces"])
    response = client.post("/purchasePlaces", data=booking_form)

    assert response.status_code == 200
    club_places_after: int = int(club["points"])
    comp_places_after: int = int(comp["numberOfPlaces"])

    assert club_places_before == club_places_after
    assert comp_places_before == comp_places_after
