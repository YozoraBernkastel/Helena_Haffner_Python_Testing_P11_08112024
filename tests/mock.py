VALID_CONNECTION: dict = {"email": "test@test.test"}
VALID_COMP: str = "Thirty Seven Places Comp"

INVALID_CONNECTION: dict = {"email": "fausseadresse@mail.com"}
INVALID_CLUB: str = "Not Existing Club"
INVALID_COMP: str = "No Existing Festival"

NO_PURCHASE_MESSAGE: bytes = b"No place purchased."
INDEX_PAGE: bytes = b"<title>GUDLFT Registration</title>"
WELCOME_PAGE: bytes = b"<title>Summary | GUDLFT Registration</title>"

THIRTY_SEVEN_PLACES_COMP = {"name": "Thirty Seven Places Comp", "date": "2027-12-21 18:36:00", "numberOfPlaces": "37"}
TWO_PLACES_COMP = {"name": "Two Places Comp", "date": "2027-12-21 18:36:00", "numberOfPlaces": "2"}
PAST_COMP = {"name": "Past Comp", "date": "2020-10-22 13:30:00", "numberOfPlaces": "13"}

MOCK_COMPETITIONS: list = [
    THIRTY_SEVEN_PLACES_COMP,
    TWO_PLACES_COMP,
    PAST_COMP
]

THIRTEEN_POINTS_CLUB: dict = {"name": "Thirteen Points Club", "email": VALID_CONNECTION["email"], "points": "13"}
FOUR_POINTS_CLUB: dict = {"name": "Four Points Club", "email": "admin@ironforge.com", "points": "4"}

MOCK_CLUBS: list = [
    THIRTEEN_POINTS_CLUB,
    FOUR_POINTS_CLUB
]
