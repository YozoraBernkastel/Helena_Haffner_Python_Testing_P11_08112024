from random import randint
from tests.mock import MOCK_COMPETITIONS, MOCK_CLUBS, MAX_PURCHASE, VALID_CLUB, VALID_COMP


def valid_places_purchase(club: dict, competition: dict) -> int:
    max_usable_club_points: int = randint(1, min(MAX_PURCHASE, int(club["points"])))
    return min(int(competition["numberOfPlaces"]), max_usable_club_points)

def check_data_existence():
    if not MOCK_COMPETITIONS:
        raise Exception("There is no competition in the mock data")
    if not MOCK_CLUBS:
        raise Exception("There is no clubs in the mock data")

def init_valid_comp_club() -> tuple[str, str]:
    check_data_existence()

    comp_name = VALID_COMP
    club_name = VALID_CLUB

    return comp_name, club_name

