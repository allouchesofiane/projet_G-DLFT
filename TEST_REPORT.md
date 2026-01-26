#  Rapport de Tests - Güdlft

## Résumé exécutif
- **Date** : 25 janvier 2026  
- **Développeur** : Sofiane Allouche  
- **Framework** : pytest 9.0.2  
- **Couverture de code** : **72%**  (≥ 60% requis)  
- **Tests totaux** : **38**  
- **Tests réussis** : **38**  
- **Tests échoués** : **0**  

---

## Détail de la couverture

### Couverture par fichier
| Fichier       | Statements | Missing | Coverage |
|---------------|------------|----------|----------|
| server.py    | 78         | 5        | 94%      |
| locustfile.py | 23        | 23       | 0%       |
| **Total**    | **101**    | **28**   | **72%**  |

>  `locustfile.py` n’est pas couvert par les tests pytest car il sert uniquement aux **tests de performance**.  
> La logique métier principale (`server.py`) est couverte à **94%**.

---

## Types de tests

### Tests unitaires (20 tests)
**Fichiers :**
- `test_bug_email_not_found.py` : 3 tests  
- `test_bug_1_points_deduction.py` : 1 test  
- `test_bug_2_past_competitions.py` : 2 tests  
- `test_bug_3_max_12_places.py` : 3 tests  
- `test_bug_4_overspending_points.py` : 2 tests  
- `test_bug_5_overbooking.py` : 2 tests  
- `test_data_loading.py` : 7 tests  

**Total tests unitaires** : **20**

---

### Tests d'intégration (8 tests)
**Fichiers :**
- `test_routes.py` : 8 tests  

**Total tests d'intégration** : **8**

---

### Tests fonctionnels (14 tests)
**Fichiers :**
- `test_booking_flow.py` : 5 tests  
- `test_phase2_public_board.py` : 5 tests   

**Total tests fonctionnels** : **10**

---

### Ratio tests unitaires : fonctionnels
**Ratio** : 20:10 = **2:1**   
> Objectif qualité respecté : les tests unitaires sont au moins deux fois plus nombreux que les tests fonctionnels.

---

## Tests par catégorie

### Bugs corrigés

 **Bug 0 : Email inexistant fait planter l'application**  
- Tests : 3  
- Statut :  Tous les tests passent  

 **Bug 1 : Points non déduits après réservation**  
- Tests : 1  
- Statut :  Tous les tests passent  

 **Bug 2 : Réservation de compétitions passées possible**  
- Tests : 2  
- Statut :  Tous les tests passent  

 **Bug 3 : Limite de 12 places non respectée**  
- Tests : 3  
- Statut :  Tous les tests passent  

 **Bug 4 : Overspending de points possible**  
- Tests : 2  
- Statut :  Tous les tests passent  

 **Bug 5 : Sur-réservation des places disponibles**  
- Tests : 2  
- Statut :  Tous les tests passent  

---

## Phase 1 - Fonctionnalités

 **Connexion par email**  
- Tests : 3  
- Statut :  Tous les tests passent  

 **Affichage des compétitions**  
- Tests : 2  
- Statut :  Tous les tests passent  

 **Réservation de places**  
- Tests : 6 (happy + sad paths)  
- Statut :  Tous les tests passent  

 **Déconnexion**  
- Tests : 1  
- Statut :  Tous les tests passent  

---

## Phase 2 - Tableau public

 **Tableau public accessible sans connexion**  
- Tests : 5  
- Statut :  Tous les tests passent  

---

## Happy Paths testés
-  Connexion avec email valide  
-  Affichage de la liste des compétitions  
-  Réservation avec points suffisants  
-  Réservation exactement 12 places  
-  Affichage du tableau public des clubs  
-  Déconnexion utilisateur  

---

## Sad Paths testés
-  Connexion avec email invalide  
-  Connexion avec email vide  
-  Réservation sans points suffisants  
-  Réservation > 12 places  
-  Réservation pour compétition passée  
-  Réservation de plus de places que disponibles  

---

## Edge Cases testés
-  Réservation exactement le nombre de points disponibles  
-  Réservation exactement 12 places  
-  Validation date future vs passée  

---

## Commandes pour lancer les tests

### Tous les tests
```bash
pytest
```
### Avec couverture
```bash
pytest --cov=. --cov-report=html --cov-report=term
```

### Tests unitaires seulement
```bash
pytest tests/unit/
```

### Tests d'intégration seulement
```bash
pytest tests/integration/
```

### Tests fonctionnels seulement
```bash
pytest tests/functional/
```

### Un fichier spécifique
```bash
pytest tests/unit/test_bug_1_points_deduction.py -v
```

## Conclusion
 Tous les critères de test sont respectés :
- Framework pytest installé 
- Tests exécutables en ligne de commande 
- Dossiers séparés unit/ et integration/ 
- Ratio 2:1 (unitaires:fonctionnels) 
- Couverture ≥ 60% 
- Phase 1 et Phase 2 entièrement testées 
- Tests unitaires pour fonctions individuelles 
- Tests d'intégration pour système complet 
- 1 fichier test par bug/fonctionnalité 