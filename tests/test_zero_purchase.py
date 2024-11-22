from tests.choice_data_helper import choose_random_club, choose_random_competition


def init_random_data() -> tuple[dict, dict, int, dict]:
    club: dict = choose_random_club()
    competition: dict = choose_random_competition()
    no_purchase: int = 0

    too_many_purchases_form: dict = {"club": club["name"],
                                     "competition": competition["name"],
                                     "places": no_purchase}

    return club, competition, no_purchase, too_many_purchases_form


def test_zero_purchase(client) -> None:
    club, comp, zero_places, booking_form = init_random_data()
    assert zero_places == 0

    club_places_before: int = int(club["points"])
    comp_places_before: int = int(comp["numberOfPlaces"])
    response = client.post("/purchasePlaces", data=booking_form)

    assert response.status_code == 200
    club_places_after: int = int(club["points"])
    comp_places_after: int = int(comp["numberOfPlaces"])

    assert club_places_before == club_places_after
    assert comp_places_before == comp_places_after
    assert b"No place purchased." in response.data
