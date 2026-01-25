def test_public_board_accessible_without_login(client):
    """
    Test que le tableau public est accessible sans connexion
    Exigence Phase 2
    """
    response = client.get('/points')
    assert response.status_code == 200


def test_public_board_displays_all_clubs(client, clubs):
    """
    Test que tous les clubs sont affichés
    """
    response = client.get('/points')
    
    assert response.status_code == 200
    # Vérifier que tous les clubs sont présents
    for club in clubs:
        assert club['name'].encode() in response.data


def test_public_board_displays_current_points(client, clubs):
    """
    Test que les points actuels sont affichés
    """
    response = client.get('/points')
    
    assert response.status_code == 200
    # Vérifier que les points sont affichés
    for club in clubs:
        assert club['points'].encode() in response.data


def test_public_board_is_read_only(client):
    """
    Test qu'on ne peut pas modifier les points depuis le tableau
    """
    response = client.get('/points')
    
    assert response.status_code == 200
    page = response.data.decode(("utf-8")).lower()
    assert 'type="number"' not in page

def test_public_board_has_link_to_home(client):
    """
    Test qu'il y a un lien pour retourner à l'accueil
    """
    response = client.get('/points')
    
    assert response.status_code == 200
    page = response.data.decode("utf-8").lower()
    assert 'href="/"' in page or 'home' in page