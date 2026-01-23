
def test_cannot_book_more_than_12_places(client):
    """
    Test qu'on ne peut pas réserver plus de 12 places
    """
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Festival',
        'places': '15'
    })
    
    assert response.status_code == 200
    page = response.data.decode().lower()
    assert "12" in page or "maximum" in page


def test_can_book_exactly_12_places(client):
    """
    Test qu'on peut réserver exactement 12 places
    """
    response = client.post('/purchasePlaces', data={
        # 18 points
        'club': 'Iron Temple',  
        'competition': 'Spring Festival',
        # Exactement 12
        'places': '12'  
    })
    
    # Assert
    assert response.status_code == 200
    
    # Vérifier qu'il n'y a pas de message d'erreur
    page = response.data.decode().lower()
    assert "maximum" not in page
    assert "vous ne pouvez pas réserver plus de 12 places" not in page


def test_can_book_less_than_12_places(client):
    """
    Test qu'on peut réserver moins de 12 places
    """
    # Act
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Festival',
        'places': '5'
    })
    
    # Assert
    assert response.status_code == 200
    # Vérifier qu'un message de succès est affiché
    page = response.data.decode().lower()
    assert "réservées" in page or "booked" in page