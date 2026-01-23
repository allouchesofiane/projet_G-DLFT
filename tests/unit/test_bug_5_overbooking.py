

def test_cannot_book_more_than_available_places(client):
    """
    On ne peut pas réserver plus de places que disponibles dans la compétition.
    """
    response = client.post("/purchasePlaces", data={
        "club": "Simply Lift",
        "competition": "Spring Festival",
        "places": "15"  
    })

    assert response.status_code == 200
    page = response.data.decode().lower()
    assert "pas assez de places" in page or "places disponibles" in page


def test_can_book_when_places_are_available(client):
    """
    On peut réserver si le nombre demandé est <= places disponibles.
    """
    response = client.post("/purchasePlaces", data={
        "club": "Simply Lift",
        "competition": "Spring Festival",
        "places": "2"
    })

    assert response.status_code == 200
    page = response.data.decode().lower()
    assert "pas assez de places" not in page
