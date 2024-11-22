from server import past_competition_places_filter

MOCK_COMPETITIONS: list = [
    {
        "name": "Spring Festival",
        "date": "2025-03-27 10:00:00",
        "numberOfPlaces": "25"
    },
    {
        "name": "Fall Classic",
        "date": "2020-10-22 13:30:00",
        "numberOfPlaces": "13"
    },
    {
        "name": "Fall Classic 五",
        "date": "2025-10-12 13:30:00",
        "numberOfPlaces": "2"
    },
    {
        "name": "Winter Lift",
        "date": "2025-12-21 18:36:00",
        "numberOfPlaces": "37"
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
MAX_PURCHASE: int = 12

