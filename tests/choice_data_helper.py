from random import choice
from server import is_competition_in_past
from tests.mock import MOCK_CLUBS, MOCK_COMPETITIONS, MAX_PURCHASE

def choose_club_with_points() -> dict:
    clubs: list = [club for club in MOCK_CLUBS if int(club["points"]) > 0]

    if len(clubs) > 0:
        return choice(clubs)

    raise Exception("There is no clubs with points")


def choose_comp_with_points() -> dict:
    comps: list = [comp for comp in MOCK_COMPETITIONS if int(comp["numberOfPlaces"]) > 0]

    if len(comps) > 0:
        return choice(comps)

    raise Exception("There is no competition with remain places")


def choose_random_club() -> dict:
    if len(MOCK_CLUBS) > 0:
        return choice(MOCK_CLUBS)

    raise Exception("There is no clubs in the data")


def choose_random_competition() -> dict:
    competitions: list = [comp for comp in MOCK_COMPETITIONS if not is_competition_in_past(comp["date"])]
    if len(competitions) > 0:
        return choice(competitions)

    raise Exception("There is no competition in the data")

def choose_club_with_more_than_twelve_points() -> dict:
    clubs: list = [club for club in MOCK_CLUBS if int(club["points"]) > MAX_PURCHASE]

    if len(clubs) > 0:
        return choice(clubs)

    raise Exception("There is no clubs with more than 12 points")


def choose_comp_with_more_than_twelve_points() -> dict:
    comps: list = [comp for comp in MOCK_COMPETITIONS if int(comp["numberOfPlaces"]) > MAX_PURCHASE]

    if len(comps) > 0:
        return choice(comps)

    raise Exception("There is no competition with more than 12 remain places")

def choose_club_with_less_than_twelve_points() -> dict:
    clubs: list = [club for club in MOCK_CLUBS if int(club["points"]) < MAX_PURCHASE]

    if len(clubs) > 0:
        return choice(clubs)

    raise Exception("There is no clubs with less than 12 points")

def choose_comp_with_less_than_twelve_points() -> dict:
    comps: list = [comp for comp in MOCK_COMPETITIONS if int(comp["numberOfPlaces"]) < MAX_PURCHASE]

    if len(comps) > 0:
        return choice(comps)

    raise Exception("There is no competition with less than 12 remain places")

def choose_random_past_competition():
    comps: list = [comp for comp in MOCK_COMPETITIONS if is_competition_in_past(comp["date"])]

    if len(comps) > 0:
        return choice(comps)

    raise Exception("There is no past competition.")