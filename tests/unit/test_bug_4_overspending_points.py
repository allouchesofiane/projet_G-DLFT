
def test_cannot_overspend_points(client, clubs):
    """
    Test qu'on ne peut pas dépenser plus de points que disponible
    """

    response = client.post('/purchasePlaces', data={
        'club': 'She Lifts',
        'competition': 'Spring Festival',
        # > 12 points disponibles
        'places': '15'
    })
    
    # Assert
    assert response.status_code == 200
    page = response.data.decode().lower()
    assert "pas assez de points" in page

def test_can_spend_available_points(client):
    """
    Test qu'on peut dépenser exactement tous ses points
    """
    response = client.post('/purchasePlaces', data={
        'club': 'She Lifts',
        'competition': 'Spring Festival',
        'places': '12'
    })
    
    # Assert
    assert response.status_code == 200
    # Ne doit pas afficher d'erreur
    page = response.data.decode().lower()
    assert "pas assez de points" not in page


