import pytest
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import server
from server import app, loadClubs, loadCompetitions


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    app.secret_key = 'test_secret_key'

    with app.test_client() as client:
        yield client


@pytest.fixture
def clubs():
    return loadClubs()


@pytest.fixture
def competitions():
    return loadCompetitions()


@pytest.fixture(autouse=True)
def restore_clubs_file():
    with open("clubs.json", "r", encoding="utf-8") as f:
        original = f.read()

    yield

    with open("clubs.json", "w", encoding="utf-8") as f:
        f.write(original)


@pytest.fixture(autouse=True)
def restore_competitions_file():
    with open("competitions.json", "r", encoding="utf-8") as f:
        original = f.read()

    yield

    with open("competitions.json", "w", encoding="utf-8") as f:
        f.write(original)


@pytest.fixture(autouse=True)
def reset_data():
    server.clubs = server.loadClubs()
    server.competitions = server.loadCompetitions()
    yield
    server.clubs = server.loadClubs()
    server.competitions = server.loadCompetitions()
