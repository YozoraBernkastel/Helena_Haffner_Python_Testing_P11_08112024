from server import is_competition_in_past, past_competition_places_filter
from tests.mock import (PAST_DATE, TOMORROW_DATE, PAST_COMP_UNLISTED,
                        FUTURE_THIRTY_SEVEN_PLACES_COMP, TODAY_TWO_PLACES_COMP)

def test_is_competition_in_past():
    is_past_comp: bool = is_competition_in_past(PAST_DATE)
    assert is_past_comp

def test_is_competition_in_future():
    is_past_comp: bool = is_competition_in_past(TOMORROW_DATE)
    assert not is_past_comp

def test_past_competition_filter_for_past_comp():
    assert int(PAST_COMP_UNLISTED["numberOfPlaces"]) > 0
    past_competition_places_filter([PAST_COMP_UNLISTED])
    assert int(PAST_COMP_UNLISTED["numberOfPlaces"]) == 0

def test_past_competition_filter_for_future_comp():
    assert int(FUTURE_THIRTY_SEVEN_PLACES_COMP["numberOfPlaces"]) > 0
    past_competition_places_filter([FUTURE_THIRTY_SEVEN_PLACES_COMP])
    assert int(FUTURE_THIRTY_SEVEN_PLACES_COMP["numberOfPlaces"]) > 0

def test_past_competition_filter_for_today_comp():
    assert int(TODAY_TWO_PLACES_COMP["numberOfPlaces"]) > 0
    past_competition_places_filter([TODAY_TWO_PLACES_COMP])
    assert int(TODAY_TWO_PLACES_COMP["numberOfPlaces"]) > 0