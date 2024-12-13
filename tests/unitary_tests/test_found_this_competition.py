from server import found_this_competition
from tests.mock import VALID_COMP, INVALID_COMP

def test_this_existing_club():
    this_club = found_this_competition(VALID_COMP)
    assert isinstance(this_club, dict)

def test_this_non_existing_club():
    this_club = found_this_competition(INVALID_COMP)
    assert this_club is None