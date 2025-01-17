from tests.mock import MOCK_COMPETITIONS, MOCK_CLUBS, THIRTEEN_POINTS_CLUB, FUTURE_THIRTY_SEVEN_PLACES_COMP


def booking_page(comp_name) -> bytes:
    booking_title = f"<title>Booking for {comp_name} || GUDLFT</title>"
    return booking_title.encode()


def welcome_club(club_name) -> bytes:
    welcome_user = f"<h2>Welcome, {club_name} </h2>"
    return welcome_user.encode()

def html_club_points(club_points) -> bytes:
    points_available = f"Points available: {club_points}"
    return points_available.encode()

def check_data_existence():
    if not MOCK_COMPETITIONS:
        raise Exception("There is no competition in the mock data")
    if not MOCK_CLUBS:
        raise Exception("There is no clubs in the mock data")

def valid_data() -> tuple[dict, dict]:
    return THIRTEEN_POINTS_CLUB, FUTURE_THIRTY_SEVEN_PLACES_COMP
