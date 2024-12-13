from datetime import date, timedelta

VALID_CONNECTION: dict = {"email": "test@test.test"}
VALID_CLUB: str = "Thirteen Points Club"
VALID_COMP: str = "Thirty Seven Places Comp"

INVALID_CONNECTION: dict = {"email": "fausseadresse@mail.com"}
INVALID_CLUB: str = "Not Existing Club"
INVALID_COMP: str = "No Existing Festival"

NO_PURCHASE_MESSAGE: bytes = b"No place purchased."
INDEX_PAGE: bytes = b"<title>GUDLFT Registration</title>"
WELCOME_PAGE: bytes = b"<title>Summary | GUDLFT Registration</title>"
POINTS_TABLE_PAGE = b"<title>Points' Table | GUDLFT</title>"
NO_PLACE_ANYMORE_MESSAGE = b"Unfortunately the last places are not available anymore"

TOMORROW_DATE = f"{date.today() + timedelta(days=1)} 18:36:00"
FUTURE_THIRTY_SEVEN_PLACES_COMP = {"name": VALID_COMP, "date": TOMORROW_DATE, "numberOfPlaces": "37"}
FUTURE_ZERO_PLACE_COMP = {"name": "No Place Comp", "date": TOMORROW_DATE, "numberOfPlaces": "0"}
TODAY_DATE = f"{date.today()} 18:36:00"
TODAY_TWO_PLACES_COMP = {"name": "Two Places Comp", "date": TODAY_DATE, "numberOfPlaces": "2"}

PAST_DATE: str = "2020-10-22 13:30:00"
PAST_COMP = {"name": "Past Comp", "date": PAST_DATE, "numberOfPlaces": "13"}
PAST_COMP_UNLISTED = {"name": "Past Comp", "date": PAST_DATE, "numberOfPlaces": "13"}

MOCK_COMPETITIONS: list = [
    FUTURE_THIRTY_SEVEN_PLACES_COMP,
    TODAY_TWO_PLACES_COMP,
    PAST_COMP,
    FUTURE_ZERO_PLACE_COMP
]

THIRTEEN_POINTS_CLUB: dict = {"name": VALID_CLUB, "email": VALID_CONNECTION["email"], "points": "13"}
FOUR_POINTS_CLUB: dict = {"name": "Four Points Club", "email": "admin@ironforge.com", "points": "4"}

MOCK_CLUBS: list = [
    THIRTEEN_POINTS_CLUB,
    FOUR_POINTS_CLUB
]

THIRTEEN_IN_STR: str = "13"
FIVE_IN_STR: str = "5"