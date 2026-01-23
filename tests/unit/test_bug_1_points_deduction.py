import json

def get_points_from_file(club_name):
    """Retourne les points d'un club (en int) en lisant clubs.json."""
    with open("clubs.json", "r") as file:
        data = json.load(file)
    for club in data["clubs"]:
        if club["name"] == club_name:
            return int(club["points"])
    # Si le club n'existe pas
    raise ValueError(f"Club introuvable dans clubs.json : {club_name}")

def test_points_are_deducted_after_booking(client):
    """
    Test que les points du club sont bien déduits après une réservation
    """
    # Données de test 
    club_name = "Simply Lift"
    competition_name = "Spring Festival"
    places_to_book = 3
    
    # Avant réservation 
    initial_points = get_points_from_file(club_name)
    
    # réservation 
    response = client.post("/purchasePlaces", data={
        "club": club_name,
        "competition": competition_name,
        "places": str(places_to_book)
    })
    
    # Après réservation 
    updated_points = get_points_from_file(club_name)
    
    # Vérifications 
    assert response.status_code == 200
    expected_points = initial_points - places_to_book
    assert updated_points == expected_points, f"Points attendus: {expected_points}, Points actuels: {updated_points}"

