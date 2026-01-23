
def test_cannot_book_past_competition(client):
    """
    Test :On ne peut pas réserver une compétition passée
    """
    # tenter de réserver une compétition passée
    response = client.post("/purchasePlaces", data={
        "club": "Simply Lift",
        # compétition passée
        "competition": "Fall Classic",  
        "places": "1"
    })

    # Vérifier que la page s'affiche
    assert response.status_code == 200

    # Vérifier qu'un message d'erreur est présent
    page = response.data.decode().lower()
    assert "passée" in page or "past" in page


def test_can_book_future_competition(client):
    """
    Test :On peut toujours réserver une compétition future
    """
    response = client.post("/purchasePlaces", data={
        "club": "Simply Lift",
        # compétition future
        "competition": "Spring Festival",  
        "places": "1"
    })

    assert response.status_code == 200

    # Ne doit PAS afficher de message d'erreur
    page = response.data.decode().lower()
    assert "passée" not in page and "past" not in page
