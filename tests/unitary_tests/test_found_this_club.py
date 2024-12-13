from server import found_this_club
from tests.mock import VALID_CLUB, INVALID_CLUB

def test_this_existing_club():
    this_club = found_this_club(VALID_CLUB)
    assert isinstance(this_club, dict)

def test_this_non_existing_club():
    this_club = found_this_club(INVALID_CLUB)
    assert this_club is None