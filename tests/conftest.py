import pytest
import sys
import os

# Ajouter le répertoire parent au path pour importer server
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from server import app, loadClubs, loadCompetitions


@pytest.fixture
def client():
    """Fixture pour tester l'application Flask"""
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    app.secret_key = 'test_secret_key'
    
    with app.test_client() as client:
        yield client


@pytest.fixture
def sample_club():
    """Fixture pour un club de test"""
    return {
        "name": "Test Club",
        "email": "test@club.com",
        "points": "10"
    }


@pytest.fixture
def sample_competition():
    """Fixture pour une compétition de test"""
    return {
        "name": "Test Competition",
        "date": "2025-03-01 10:00:00",
        "numberOfPlaces": "25"
    }


@pytest.fixture
def clubs():
    """Fixture pour charger les clubs"""
    return loadClubs()


@pytest.fixture
def competitions():
    """Fixture pour charger les compétitions"""
    return loadCompetitions()


@pytest.fixture(autouse=True)
def restore_clubs_file():
    # Sauvegarde avant test
    with open("clubs.json", "r", encoding="utf-8") as f:
        original = f.read()

    yield

    # Restauration après test
    with open("clubs.json", "w", encoding="utf-8") as f:
        f.write(original)