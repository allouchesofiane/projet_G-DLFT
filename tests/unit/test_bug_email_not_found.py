"""
Tests pour le bug : Email inexistant fait planter l'application
"""


def test_invalid_email_does_not_crash_app(client):
    """
    Test qu'un email invalide ne fait pas planter l'application
    """
    # Arrange : préparer les données
    invalid_email = "sofianeallouche@yahoo.com"

    # Act : envoyer le formulaire
    response = client.post("/showSummary", data={"email": invalid_email})

    # Assert : vérifier le résultat
    assert response.status_code == 200

    # Convertir la réponse en texte lisible
    page = response.data.decode("utf-8")

    # Vérifier qu'un message lié à l'email est affiché
    assert "email" in page.lower()

    # Vérifier que le formulaire est toujours présent (page d'accueil)
    assert "<form" in page


def test_valid_email_still_works(client):
    """
    Test qu'un email valide fonctionne toujours après la correction
    """
    # Arrange
    valid_email = "john@simplylift.co"

    # Act
    response = client.post("/showSummary", data={"email": valid_email})

    # Assert
    assert response.status_code == 200

    page = response.data.decode("utf-8")
    assert "simply lift" in page.lower() or "welcome" in page.lower()


def test_empty_email_handled(client):
    """
    Test que l'envoi d'un email vide est géré
    """
    # Arrange
    empty_email = ""

    # Act
    response = client.post("/showSummary", data={"email": empty_email})

    # Assert
    assert response.status_code == 200

    page = response.data.decode("utf-8")
    assert "<form" in page
