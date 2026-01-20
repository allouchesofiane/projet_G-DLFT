# Liste des bugs à corriger

## Bug 1 : Email inexistant fait planter l'application
- **Description :** IndexError quand email n'existe pas
- **Comment reproduire :** 
  1. Aller sur page d'accueil
  2. Entrer email inexistant (ex: sofianeallouche@yahoo.com)
  3. Application plante

## Bug 2 : Points non déduits
- **Description :** Les points du club ne sont pas déduits après réservation
- **Comment reproduire :**
  1. Se connecter avec john@simplylift.co (13 points)
  2. Réserver 3 places
  3. Vérifier clubs.json → points toujours à 13

## Bug 3 : Réservation pour compétitions passées
- **Description :** Peut réserver des places pour une compétition déjà passée
- **Comment reproduire :**
  1. Se connecter
  2. Réserver pour "Fall Classic" (date passée)
  3. Réservation acceptée (ne devrait pas)

## Bug 4 : Pas de limite à 12 places
- **Description :** Peut réserver plus de 12 places par compétition
- **Comment reproduire :**
  1. Se connecter avec john@simplylift.co (13 points)
  2. Réserver 15 places
  3. Réservation acceptée (devrait être refusée)

## Bug 5 : Overspending de points
- **Description :** Peut dépenser plus de points que disponible
- **Comment reproduire :**
  1. Se connecter avec kate@shelifts.co.uk (12 points)
  2. Réserver 15 places
  3. Réservation acceptée (devrait être refusée)

## Bug 6 : Réservation par rapport aux places restantes
- **Description :** L’utilisateur peut réserver plus de places que competition['numberOfPlaces'] restantes.
- **Comment reproduire :**
  1. Se connecter
  2. Choisir une compétition avec peu de places restantes (ex : 13)
  3. Demander 20 places
  4. Réservation acceptée (ne devrait pas)

## Fonctionnalité manquante
### Tableau public des points
- **Description :** Afficher un tableau de tous les clubs avec leurs points
- **Exigences :**
  - Accessible sans connexion
  - Affiche tous les clubs
  - Affiche points actualisés
