

def test_cannot_overspend_points(client):
    """
    Iron Temple a 4 points -> on tente 5 places (5 points)
    => doit refuser avec "pas assez de points"
    """
    response = client.post("/purchasePlaces", data={
        "club": "Iron Temple",
        "competition": "Spring Festival",
        "places": "5"
    })

    assert response.status_code == 200
    page = response.data.decode().lower()
    assert "pas assez de points" in page


def test_can_spend_available_points(client):
    """
    Iron Temple a 4 points -> on réserve exactement 4 places
    => doit passer (pas de message "pas assez de points")
    """
    response = client.post("/purchasePlaces", data={
        "club": "Iron Temple",
        "competition": "Spring Festival",
        "places": "4"
    })

    assert response.status_code == 200
    page = response.data.decode().lower()
    assert "pas assez de points" not in page



