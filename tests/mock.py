from random import randint

MOCK_COMPETITIONS: list = [
    {
        "name": "Winter Festival",
        "date": "2020-03-27 10:00:00",
        "numberOfPlaces": "25"
    },
    {
        "name": "Fall Vanilla",
        "date": "2020-10-22 13:30:00",
        "numberOfPlaces": "13"
    }
]

MOCK_CLUBS: list = [
    {
        "name": "Test Name",
        "email": "test@test.test",
        "points": "13"
    },
    {
        "name": "Iron Forge",
        "email": "admin@ironforge.com",
        "points": "4"
    },
    {
        "name": "He Leafs",
        "email": "cakeisalie@aperture.com",
        "points": "12"
    }
]

VALID_CONNECTION: dict = {"email": "test@test.test"}
INVALID_CONNECTION: dict = {"email": "fausseadresse@mail.com"}


CLUB = MOCK_CLUBS[0]
COMPETITION = MOCK_COMPETITIONS[0]
VALID_PLACES = randint(1, max(12, int(CLUB["points"])))

VALID_POINTS_BOOKING: dict = {"club": CLUB["name"],
                              "competition": COMPETITION["name"],
                              "places": VALID_PLACES}

