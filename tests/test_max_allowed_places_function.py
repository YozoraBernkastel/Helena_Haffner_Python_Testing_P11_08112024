from server import max_allowed_places, MAX_PLACES
from tests.mock import THIRTEEN_IN_STR, FIVE_IN_STR

def test_twelve_places_max():
    max_allowed = max_allowed_places(THIRTEEN_IN_STR, THIRTEEN_IN_STR)
    assert max_allowed == MAX_PLACES

def test_comp_places_are_too_low():
    max_allowed = max_allowed_places(THIRTEEN_IN_STR, FIVE_IN_STR)
    assert max_allowed == int(FIVE_IN_STR)

def test_club_points_purchases_lower_than_places():
    max_allowed = max_allowed_places(FIVE_IN_STR, THIRTEEN_IN_STR)
    assert max_allowed == int(FIVE_IN_STR)

def test_club_purchases_all_places_under_twelve():
    max_allowed = max_allowed_places(FIVE_IN_STR, FIVE_IN_STR)
    assert max_allowed == int(FIVE_IN_STR)