from flask import url_for, request
from tests.mock import INDEX_PAGE, WELCOME_PAGE, THIRTEEN_POINTS_CLUB, FUTURE_ZERO_PLACE_COMP, NO_PLACE_ANYMORE_MESSAGE
from tests.data_helper import welcome_club, booking_page


def test_user_wants_to_purchase(client, mock_clubs, mock_competitions):
    user_club: dict = THIRTEEN_POINTS_CLUB
    zero_place_comp = FUTURE_ZERO_PLACE_COMP
    purchase_places = 1

    first_response = client.get("/")
    assert first_response.status_code == 200
    assert INDEX_PAGE in first_response.data

    second_response = client.post("/showSummary", data={"email": user_club["email"]})
    assert second_response.status_code == 200
    assert WELCOME_PAGE in second_response.data
    assert welcome_club(user_club["email"]) in second_response.data

    third_response = client.get(f"/book/{zero_place_comp['name']}/{user_club['name']}")
    assert third_response.status_code == 200
    assert booking_page(zero_place_comp["name"]) in third_response.data

    valid_booking_form: dict = {"club": user_club["name"],
                                "competition": zero_place_comp["name"],
                                "places": purchase_places}

    club_points_before: int = int(user_club["points"])
    comp_places_before: int = int(zero_place_comp["numberOfPlaces"])
    fourth_response = client.post("/purchasePlaces", data=valid_booking_form)

    assert fourth_response.status_code == 200
    assert WELCOME_PAGE in fourth_response.data
    assert NO_PLACE_ANYMORE_MESSAGE in fourth_response.data
    assert welcome_club(user_club["email"]) in fourth_response.data

    club_points_after: int = int(user_club["points"])
    comp_places_after: int = int(zero_place_comp["numberOfPlaces"])

    assert club_points_before == club_points_after
    assert comp_places_before == comp_places_after

    fifth_response = client.get("/logout")
    assert fifth_response.status_code == 302
    assert request.path == url_for('logout')

    # reset data
    user_club["points"] = str(club_points_before)
    zero_place_comp["numberOfPlaces"] = str(comp_places_before)
