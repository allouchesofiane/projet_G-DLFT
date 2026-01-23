import json
import server


def _set_competition_places(name: str, places: int) -> None:
    """Force numberOfPlaces dans competitions.json et recharge server.competitions."""
    with open("competitions.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    comp = next(c for c in data["competitions"] if c["name"].lower() == name.lower())
    comp["numberOfPlaces"] = str(places)

    with open("competitions.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    # recharger les données en mémoire
    server.competitions = server.loadCompetitions()


def test_cannot_book_more_than_available_places(client):
    """
    On ne peut pas réserver plus de places que disponibles dans la compétition.
    """
    _set_competition_places("Spring Festival", 2)

    response = client.post("/purchasePlaces", data={
        "club": "Simply Lift",
        "competition": "Spring Festival",
        "places": "10"
    })

    assert response.status_code == 200
    page = response.data.decode().lower()
    assert "pas assez de places" in page or "places disponibles" in page


def test_can_book_when_places_are_available(client):
    """
    On peut réserver si le nombre demandé est <= places disponibles.
    """
    _set_competition_places("Spring Festival", 5)

    response = client.post("/purchasePlaces", data={
        "club": "Simply Lift",
        "competition": "Spring Festival",
        "places": "2"
    })

    assert response.status_code == 200
    page = response.data.decode().lower()
    assert "pas assez de places" not in page
