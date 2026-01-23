import json
from flask import Flask,render_template,request,redirect,flash,url_for

def save_clubs(clubs_data):
    """Sauvegarde les données des clubs dans clubs.json"""
    with open('clubs.json', 'w') as f:
        json.dump({'clubs': clubs_data}, f, indent=4)

def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary', methods=['POST'])
def showSummary():
    """
    Affiche le résumé pour un club connecté
    Gère le cas où l'email n'existe pas (bug critique corrigé)
    """
    email = request.form.get('email', '')
    
    # Chercher le club avec cet email
    club_list = [c for c in clubs if c['email'] == email]
    
    # Vérifier si le club existe
    if not club_list:
        flash("Désolé, cette adresse email est introuvable. Veuillez réessayer.")
        return render_template('index.html')
    
    # Club trouvé
    club = club_list[0]
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    # Achete les places pour une compétition
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    # Deduire les places de la compétition
    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
    # Déduire les points du club
    club['points'] = str(int(club['points']) - placesRequired)
    
    # Sauvegarder les modifications dans clubs.json
    save_clubs(clubs)
    
    flash(f'Great! {placesRequired} places booked for {competition["name"]}')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
