from server import MAX_PLACES
from tests.data_helper import valid_data


def init_data() -> tuple[dict, dict, int, dict]:
    club, competition = valid_data()
    valid_places: int = MAX_PLACES

    valid_booking_form: dict = {"club": club["name"],
                                "competition": competition["name"],
                                "places": valid_places}

    return club, competition, valid_places, valid_booking_form


def test_points_and_places_update(client, mock_clubs, mock_competitions) -> None:
    club, comp, places_number, booking_form = init_data()

    club_points_before: int = int(club["points"])
    comp_places_before: int = int(comp["numberOfPlaces"])
    response = client.post("/purchasePlaces", data=booking_form)

    assert response.status_code == 200

    club_points_after: int = int(club["points"])
    comp_places_after: int = int(comp["numberOfPlaces"])
    check_points_computation: bool = club_points_after == club_points_before - places_number
    check_places_computation: bool = comp_places_after == comp_places_before - places_number

    assert club_points_before > club_points_after and check_points_computation
    assert comp_places_before > comp_places_after and check_places_computation

    # reset data as we want correct data for the next units tests
    club["points"] = str(club_points_before)
    comp["numberOfPlaces"] = str(comp_places_before)
