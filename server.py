import json
from datetime import date, datetime
from flask import Flask, render_template, request, redirect, flash, url_for

MIN_PLACES: int = 1
MAX_PLACES: int = 12
TODAY = date.today()


def load_clubs():
    with open('clubs.json') as c:
        list_of_clubs = json.load(c)['clubs']
        return list_of_clubs


def is_competition_in_past(competition_date: str) -> bool:
    competition_date = datetime.strptime(competition_date[:10], '%Y-%m-%d').date()
    return competition_date < TODAY


def past_competition_places_filter(competitions_list: list) -> None:
    for comp in competitions_list:
        if is_competition_in_past(comp["date"]):
            comp["numberOfPlaces"] = 0


def load_competitions():
    with open('competitions.json') as comps:
        list_of_competitions = json.load(comps)['competitions']
        past_competition_places_filter(list_of_competitions)
        return list_of_competitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions: list = load_competitions()
clubs: list = load_clubs()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def show_summary():
    for club in clubs:
        if club['email'] == request.form['email']:
            return render_template('welcome.html', club=club, competitions=competitions)

    flash("Sorry, that email wasn't found.")
    return index()

def max_allowed_places(club_point: str, comp_places: str) -> int:
    limit_places: int = min(int(club_point), int(comp_places))
    return min(MAX_PLACES, limit_places)


@app.route('/book/<competition>/<club>')
def book(competition, club):
    found_club = [c for c in clubs if c['name'] == club]
    found_competition = [c for c in competitions if c['name'] == competition]

    if not found_club or not found_competition:
        flash("Something went wrong-please try again")
        if found_club:
            return render_template('welcome.html', club=club, competitions=competitions)
        else:
            return render_template('index.html')

    this_club = found_club[0]
    this_competition = found_competition[0]
    max_allowed = max_allowed_places(this_club["points"], this_competition["numberOfPlaces"])

    return render_template('booking.html', club=this_club,
                           competition=this_competition, max_allowed=max_allowed)


@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    competition = [c for c in competitions if c['name'] == request.form['competition']]
    club = [c for c in clubs if c['name'] == request.form['club']]

    if not club or not competition:
        flash("Something went wrong-please try again")
        return render_template('index.html')

    this_club = club[0]
    this_competition = competition[0]
    places_required = int(request.form['places'])

    if is_competition_in_past(this_competition["date"]):
        flash("no place attribute ... the competition is already done.")
        return render_template('welcome.html', club=this_club, competitions=competitions)

    max_allowed = max_allowed_places(this_club["points"], this_competition["numberOfPlaces"])

    if MIN_PLACES <= places_required <= max_allowed:
        this_club["points"] = int(this_club["points"]) - places_required
        this_competition['numberOfPlaces'] = int(this_competition['numberOfPlaces']) - places_required
        flash('Great-booking complete!')
        return render_template('welcome.html', club=this_club, competitions=competitions)

    # This part of the code can only be reached if the user purchase 0 place or if they manually
    # change the HTML code, so we always want to give no place at this point.
    flash("No place purchased.")
    return render_template('welcome.html', club=this_club, competitions=competitions)


# TODO: Add route for points display

@app.route('/logout')
def logout():
    return redirect(url_for('index'))

#  todo faire les tests unitaires pour véririfer que l'on est bien renvoyé sur la page index si aucun nom de club ou de compétition n'est trouvé dans la bdd
