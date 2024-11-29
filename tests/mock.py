VALID_CONNECTION: dict = {"email": "test@test.test"}
VALID_CLUB: str = "Test Name"
VALID_COMP: str = "Spring Fest ival"

INVALID_CONNECTION: dict = {"email": "fausseadresse@mail.com"}
INVALID_CLUB: str = "Not Existing Club"
INVALID_COMP: str = "No Existing Festival"
MAX_PURCHASE: int = 12

INDEX_PAGE: bytes = b"<title>GUDLFT Registration</title>"
WELCOME_PAGE: bytes = b"<title>Summary | GUDLFT Registration</title>"

def booking_page(comp_name) -> bytes:
    booking_title = f"<title>Booking for {comp_name} || GUDLFT</title>"
    return booking_title.encode()


MOCK_COMPETITIONS: list = [
    {
        "name": VALID_COMP,
        "date": "2030-03-27 10:00:00",
        "numberOfPlaces": "25"
    },
    {
        "name": "Fall Clas sic",
        "date": "2020-10-22 13:30:00",
        "numberOfPlaces": "13"
    },
    {
        "name": "Fall Clas sic 五",
        "date": "2020-10-12 13:30:00",
        "numberOfPlaces": "2"
    },
    {
        "name": "Winter Le ft",
        "date": "2020-12-21 18:36:00",
        "numberOfPlaces": "37"
    }
]

MOCK_CLUBS: list = [
    {
        "name": VALID_CLUB,
        "email": VALID_CONNECTION["email"],
        "points": "13"
    },
    {
        "name": "Irooon Forge",
        "email": "admin@ironforge.com",
        "points": "4"
    },
    {
        "name": "He Liiieafs",
        "email": "cakeisalie@aperture.com",
        "points": "12"
    }
]


