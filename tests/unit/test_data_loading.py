from server import loadClubs, loadCompetitions


def test_load_clubs_returns_list():
    """Test que loadClubs retourne une liste"""
    clubs = loadClubs()
    assert isinstance(clubs, list)
    assert len(clubs) > 0


def test_load_clubs_contains_required_fields():
    """Test que chaque club a les champs requis"""
    clubs = loadClubs()
    for club in clubs:
        assert 'name' in club
        assert 'email' in club
        assert 'points' in club


def test_load_clubs_points_are_numeric():
    """Test que les points sont des chaînes représentant des nombres"""
    clubs = loadClubs()
    for club in clubs:
        assert club['points'].isdigit()


def test_load_competitions_returns_list():
    """Test que loadCompetitions retourne une liste"""
    competitions = loadCompetitions()
    assert isinstance(competitions, list)
    assert len(competitions) > 0


def test_load_competitions_contains_required_fields():
    """Test que chaque compétition a les champs requis"""
    competitions = loadCompetitions()
    for comp in competitions:
        assert 'name' in comp
        assert 'date' in comp
        assert 'numberOfPlaces' in comp


def test_load_competitions_date_format():
    """Test que les dates sont au bon format"""
    from datetime import datetime
    
    competitions = loadCompetitions()
    for comp in competitions:
        # Ne doit pas lever d'exception
        datetime.strptime(comp['date'], '%Y-%m-%d %H:%M:%S')


def test_load_competitions_places_are_numeric():
    """Test que numberOfPlaces est une chaîne numérique"""
    competitions = loadCompetitions()
    for comp in competitions:
        assert comp['numberOfPlaces'].isdigit()