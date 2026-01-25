
from locust import HttpUser, task, between


class GudlftUser(HttpUser):
    """Simule un utilisateur de l'application GÜDLFT"""
    
    wait_time = between(1, 3)  # Pause entre les actions
    
    def on_start(self):
        """Actions au démarrage (connexion)"""
        self.client.post("/showSummary", data={
            "email": "john@simplylift.co"
        })
    
    @task(5)
    def view_index(self):
        """Test page d'accueil"""
        self.client.get("/")
    
    @task(3)
    def view_competitions_list(self):
        """
        Test affichage liste compétitions
        Exigence : < 5 secondes
        """
        with self.client.get("/", catch_response=True) as response:
            if response.elapsed.total_seconds() > 5:
                response.failure(f"Took {response.elapsed.total_seconds()}s (> 5s)")
    
    @task(2)
    def view_public_points_board(self):
        """
        Test tableau public des points
        Exigence : < 5 secondes
        """
        with self.client.get("/points", catch_response=True) as response:
            if response.elapsed.total_seconds() > 5:
                response.failure(f"Took {response.elapsed.total_seconds()}s (> 5s)")
    
    @task(1)
    def book_places(self):
        """
        Test réservation de places
        Exigence : < 2 secondes pour mise à jour
        """
        with self.client.post("/purchasePlaces", data={
            "club": "Simply Lift",
            "competition": "Spring Festival",
            "places": "1"
        }, catch_response=True) as response:
            if response.elapsed.total_seconds() > 2:
                response.failure(f"Took {response.elapsed.total_seconds()}s (> 2s)")