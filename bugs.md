# Liste des bugs à corriger

## Bug 1 : Email inexistant fait planter l'application
- **Description :** IndexError quand email n'existe pas
- **Comment reproduire :** 
  1. Aller sur page d'accueil
  2. Entrer email inexistant (ex: sofianeallouche@yahoo.com)
  3. Application plante

**Reproduction confirmée :** 
**Résultat observé :** Le serveur Flask affiche une exception IndexError sur la ligne de récupération du club.
**Fichier server.py**

## Bug 2 : Points non déduits
- **Description :** Les points du club ne sont pas déduits après réservation
- **Comment reproduire :**
  1. Se connecter avec john@simplylift.co (13 points)
  2. Réserver 3 places
  3. Vérifier clubs.json → points toujours à 13

**Reproduction confirmée :** 
**Résultat observé :** 
  1. Après la réservation de 3 places avec le club Simply Lift (13 points initiaux), la page de confirmation s’affiche correctement.
  2. Le fichier clubs.json reste inchangé.
  3. Le champ "points" du club reste à "13" au lieu de passer à "10".
**Fichier clubs.json inchangé non mis à jour**

## Bug 3 : Réservation pour compétitions passées
- **Description :** Peut réserver des places pour une compétition déjà passée
- **Comment reproduire :**
  1. Se connecter
  2. Réserver pour "Fall Classic" (date passée)
  3. Réservation acceptée (ne devrait pas)

**Reproduction confirmée :** 
**Résultat observé :** 
  1. La réservation pour la compétition Fall Classic (date passée) est acceptée sans aucune validation.
  2. Aucun message d’erreur ou d’avertissement n’est affiché à l’utilisateur.
  3. Les places sont déduites malgré la date invalide.
**Fichier server.py**

## Bug 4 : Pas de limite à 12 places
- **Description :** Peut réserver plus de 12 places par compétition
- **Comment reproduire :**
  1. Se connecter avec john@simplylift.co (13 points)
  2. Réserver 15 places
  3. Réservation acceptée (devrait être refusée)

**Reproduction confirmée :** 
**Résultat observé :** 
  1. Une demande de réservation de 15 places est acceptée.
  2. Aucun message d’erreur n’est affiché.
  3. Le stock de places de la compétition est réduit de 15, ce qui viole la règle métier “max 12 places par club”.
**Fichier server.py**

## Bug 5 : Overspending de points
- **Description :** Peut dépenser plus de points que disponible
- **Comment reproduire :**
  1. Se connecter avec kate@shelifts.co.uk (12 points)
  2. Réserver 15 places
  3. Réservation acceptée (devrait être refusée)

**Reproduction confirmée :** 
**Résultat observé :** 
 1. Le club She Lifts (12 points) peut réserver 15 places.
 2. Les points deviennent négatifs ou incohérents dans le flux applicatif.
 3. Aucun message d’erreur ou de validation n’empêche l’opération.
**Fichier server.py et club.json**

## Bug 6 : Réservation par rapport aux places restantes
- **Description :** L’utilisateur peut réserver plus de places que competition['numberOfPlaces'] restantes.
- **Comment reproduire :**
  1. Se connecter
  2. Choisir une compétition avec peu de places restantes (ex : 13)
  3. Demander 20 places
  4. Réservation acceptée (ne devrait pas)

**Reproduction confirmée :** 
**Résultat observé :** 
  1. Une demande de réservation supérieure au nombre de places restantes est acceptée.
  2. Exemple : Compétition Spring Festival avec 25 places restantes → réservation de 99 places possible.
  3. Le champ "numberOfPlaces" devient négatif ou incohérent.
  4. Aucun message d’erreur n’est affiché à l’utilisateur.
**Fichier server.py et competition.json**

## Fonctionnalité manquante
### Tableau public des points
- **Description :** Afficher un tableau de tous les clubs avec leurs points
- **Exigences :**
  - Accessible sans connexion
  - Affiche tous les clubs
  - Affiche points actualisés

### Plan de correction

# Ordre de traitement
1. **Bug 1** (critique) : Email inexistant → Bloque l'utilisation
2. **Bug 2** : Points non déduits → Fonctionnalité majeure
3. **Bug 3** : Compétitions passées → Logique métier
4. **Bug 4** : Limite 12 places → Règle métier
5. **Bug 5** : Overspending → Règle métier
6. **Bug 6** : Sur-réservation → Intégrité des données
7. **Phase 2** : Tableau public → Nouvelle fonctionnalité

## Approche
- 1 branche par bug
- Merge dans main après chaque correction