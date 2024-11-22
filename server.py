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
    found_club = [c for c in clubs if c['name'] == club][0]
    found_competition = [c for c in competitions if c['name'] == competition][0]

    if found_club and found_competition:
        max_allowed = max_allowed_places(found_club["points"], found_competition["numberOfPlaces"])
        return render_template('booking.html', club=found_club,
                               competition=found_competition, max_allowed=max_allowed)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)

@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    places_required = int(request.form['places'])

    if club and competition:
        if is_competition_in_past(competition["date"]):
            flash("no place attribute ... the competition is already done.")
            return render_template('welcome.html', club=club, competitions=competitions)

        max_allowed = max_allowed_places(club["points"], competition["numberOfPlaces"])

        if MIN_PLACES <= places_required <= max_allowed:
            club["points"] = int(club["points"]) - places_required
            competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
            flash('Great-booking complete!')
            return render_template('welcome.html', club=club, competitions=competitions)

    # This part of the code can only be reached if the user purchase 0 place or if they manually
    # change the HTML code, so we always want to give no place at this point.
    flash("No place purchased.")
    return render_template('welcome.html', club=club, competitions=competitions)

# TODO: Add route for points display

@app.route('/logout')
def logout():
    return redirect(url_for('index'))
