from server import comp_still_has_available_places
from tests.mock import FUTURE_THIRTY_SEVEN_PLACES_COMP, FUTURE_ZERO_PLACE_COMP


def test_comp_still_has_available_places():
    has_places = comp_still_has_available_places(FUTURE_THIRTY_SEVEN_PLACES_COMP)
    assert has_places

def test_comp_has_no_available_places():
    has_places = comp_still_has_available_places(FUTURE_ZERO_PLACE_COMP)
    assert not has_places