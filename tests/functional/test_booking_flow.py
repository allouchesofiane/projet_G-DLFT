def test_complete_booking_happy_path(client):
    """
    Parcours complet : connexion + réservation + confirmation + déconnexion
    """
    # Connexion
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert response.status_code == 200
    page = response.data.decode().lower()
    assert "simply lift" in page or "welcome" in page

    # Page de réservation
    response = client.get('/book/Spring Festival/Simply Lift')
    assert response.status_code == 200
    page = response.data.decode().lower()
    assert "spring festival" in page

    # Réservation
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Festival',
        'places': '2'
    })
    assert response.status_code == 200
    page = response.data.decode().lower()
    assert "réserv" in page or "booked" in page or "great" in page

    # Déconnexion
    response = client.get('/logout')
    assert response.status_code in (200, 302)


def test_booking_insufficient_points_sad_path(client):
    """
    Tentative de réservation sans points suffisants
    """
    response = client.post('/showSummary', data={'email': 'kate@shelifts.co.uk'})
    assert response.status_code == 200

    # pour tester les points, il faut rester <= 12 places,
    # sinon on déclenches la règle "max 12" avant "points insuffisants".
    response = client.post('/purchasePlaces', data={
        'club': 'Iron Temple',          # 4 points
        'competition': 'Spring Festival',
        'places': '5'                   # <= 12 mais > 4 => points insuffisants
    })
    assert response.status_code == 200
    page = response.data.decode().lower()
    assert "pas assez de points" in page or "not enough points" in page


def test_booking_too_many_places_sad_path(client):
    """
    Tentative de réservation > 12 places
    """
    response = client.post('/showSummary', data={'email': 'admin@irontemple.com'})
    assert response.status_code == 200

    response = client.post('/purchasePlaces', data={
        'club': 'Iron Temple',
        'competition': 'Spring Festival',
        'places': '20'
    })
    assert response.status_code == 200
    page = response.data.decode().lower()
    assert "limite" in page or "12" in page or "maximum" in page


def test_invalid_email_login_sad_path(client):
    """
    Connexion avec email invalide
    """
    response = client.post('/showSummary', data={'email': 'wrong@email.com'})
    assert response.status_code == 200
    page = response.data.decode().lower()
    assert "introuvable" in page or "not found" in page
    assert "<form" in page  # reste sur la page d'accueil


def test_booking_past_competition_sad_path(client):
    """
    Tentative de réservation pour une compétition passée
    """
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert response.status_code == 200

    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Fall Classic',
        'places': '1'
    })
    assert response.status_code == 200
    page = response.data.decode().lower()
    assert "passée" in page or "past" in page or "cannot book" in page
