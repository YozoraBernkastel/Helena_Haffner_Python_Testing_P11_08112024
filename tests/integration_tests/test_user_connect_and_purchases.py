from flask import url_for, request
from tests.mock import INDEX_PAGE, WELCOME_PAGE, THIRTEEN_POINTS_CLUB, FUTURE_THIRTY_SEVEN_PLACES_COMP
from tests.data_helper import welcome_club, booking_page


def test_user_wants_to_purchase(client, mock_clubs, mock_competitions):
    user_club: dict = THIRTEEN_POINTS_CLUB
    valid_comp = FUTURE_THIRTY_SEVEN_PLACES_COMP
    purchase_places = 1

    first_response = client.get("/")
    assert first_response.status_code == 200
    assert INDEX_PAGE in first_response.data

    second_response = client.post("/showSummary", data={"email": user_club["email"]})
    assert second_response.status_code == 200
    assert WELCOME_PAGE in second_response.data
    assert welcome_club(user_club["email"]) in second_response.data

    third_response = client.get(f"/book/{valid_comp['name']}/{user_club['name']}")
    assert third_response.status_code == 200
    assert booking_page(valid_comp["name"]) in third_response.data

    valid_booking_form: dict = {"club": user_club["name"],
                                "competition": valid_comp["name"],
                                "places": purchase_places}

    club_points_before: int = int(user_club["points"])
    comp_places_before: int = int(valid_comp["numberOfPlaces"])
    fourth_response = client.post("/purchasePlaces", data=valid_booking_form)

    assert fourth_response.status_code == 200
    assert WELCOME_PAGE in fourth_response.data
    assert welcome_club(user_club["email"]) in fourth_response.data

    club_points_after: int = int(user_club["points"])
    comp_places_after: int = int(valid_comp["numberOfPlaces"])
    check_points_computation: bool = club_points_after == club_points_before - purchase_places
    check_places_computation: bool = comp_places_after == comp_places_before - purchase_places

    assert club_points_before > club_points_after and check_points_computation
    assert comp_places_before > comp_places_after and check_places_computation

    fifth_response = client.get("/logout")
    assert fifth_response.status_code == 302
    assert request.path == url_for('logout')

    # reset data
    user_club["points"] = str(club_points_before)
    valid_comp["numberOfPlaces"] = str(comp_places_before)
