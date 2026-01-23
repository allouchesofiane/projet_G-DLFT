

def test_index_route_renders(client):
    """Test que la page d'accueil s'affiche"""
    response = client.get('/')

    assert response.status_code == 200

    page = response.data.decode().lower()
    assert "welcome" in page
    assert "<form" in page


def test_show_summary_with_valid_email(client):
    """Test connexion avec email valide"""
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})

    assert response.status_code == 200

    page = response.data.decode().lower()
    assert "simply lift" in page or "welcome" in page


def test_show_summary_with_invalid_email(client):
    """Test connexion avec email invalide"""
    response = client.post('/showSummary', data={'email': 'invalid@email.com'})

    assert response.status_code == 200

    page = response.data.decode().lower()
    assert "introuvable" in page or "not found" in page


def test_book_route_displays_form(client):
    """Test que la page de réservation s'affiche"""
    response = client.get('/book/Spring Festival/Simply Lift')

    assert response.status_code == 200

    page = response.data.decode().lower()
    assert "spring festival" in page
    assert "simply lift" in page


def test_purchase_places_success(client):
    """Test réservation réussie"""
    response = client.post('/purchasePlaces', data={
        'club': 'Iron Temple',
        'competition': 'Spring Festival',
        'places': '2'
    })

    assert response.status_code == 200

    page = response.data.decode().lower()
    assert "réservées" in page or "booked" in page or "success" in page


def test_purchase_places_insufficient_points(client):
    """Test réservation sans points suffisants"""
    response = client.post('/purchasePlaces', data={
        'club': 'She Lifts',
        'competition': 'Spring Festival',
        'places': '15'
    })

    assert response.status_code == 200

    page = response.data.decode().lower()
    assert "pas assez de points" in page or "not enough points" in page


def test_purchase_places_more_than_12(client):
    """Test réservation > 12 places"""
    response = client.post('/purchasePlaces', data={
        'club': 'Iron Temple',
        'competition': 'Spring Festival',
        'places': '15'
    })

    assert response.status_code == 200

    page = response.data.decode().lower()
    assert "12" in page or "maximum" in page or "limite" in page


def test_logout_redirects_to_index(client):
    """Test déconnexion"""
    response = client.get('/logout')

    # Doit rediriger vers index
    assert response.status_code in (200, 302)
