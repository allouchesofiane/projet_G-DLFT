# 📊 Rapport de Performance - Güdlft

## Configuration des tests
- **Outil** : Locust 2.43.1  
- **Nombre d'utilisateurs simultanés** : 6  
- **Spawn rate** : 1 utilisateur/seconde  
- **Durée du test** : 5 minutes  
- **URL cible** : http://127.0.0.1:5000  
- **Date** : 25/01/2026  

---

## Exigences de performance
-  Chargement liste compétitions : < 5000 ms  
-  Mise à jour points : < 2000 ms  

---

## Résultats

### 1. Page d'accueil (GET /)
| Métrique | Valeur | Conformité |
|----------|--------|------------|
| Temps de réponse moyen | **5,56 ms** |  < 5000 ms |
| Temps de réponse médian | **5 ms** |  |
| 95e percentile | **7 ms** |  |
| Temps de réponse max | **83 ms** |  |
| Nombre total de requêtes | **823** | - |
| Nombre d'échecs | **0** |  |
| Requests/seconde | **1,7 rps** | - |

---

### 2. Liste compétitions (POST /showSummary)
| Métrique | Valeur | Conformité |
|----------|--------|------------|
| Temps de réponse moyen | **6,17 ms** |  < 5000 ms |
| Temps de réponse médian | **5 ms** |  |
| 95e percentile | **9 ms** |  
| Temps de réponse max | **9 ms** |  
| Nombre total de requêtes | **6** | 
| Nombre d'échecs | **0** | 
| Requests/seconde | **0 rps** | 

---

### 3. Tableau public (GET /points)
| Métrique | Valeur | Conformité |
|----------|--------|------------|
| Temps de réponse moyen | **6,06 ms** |  < 5000 ms |
| Temps de réponse médian | **5 ms** |  
| 95e percentile | **9 ms** |
| Temps de réponse max | **23 ms** | 
| Nombre total de requêtes | **189** | 
| Nombre d'échecs | **0** | 
| Requests/seconde | **0,7 rps** | 

---

### 4. Réservation places (POST /purchasePlaces)
| Métrique | Valeur | Conformité |
|----------|--------|------------|
| Temps de réponse moyen | **6,03 ms** |  < 2000 ms |
| Temps de réponse médian | **6 ms** |  |
| 95e percentile | **8 ms** | 
| Temps de réponse max | **21 ms** | 
| Nombre total de requêtes | **110** | 
| Nombre d'échecs | **0** | 
| Requests/seconde | **0,4 rps** | 

---

## Graphiques
```text
./screenshots

## Analyse

### Points forts
-  Tous les endpoints respectent les exigences de performance
-  Aucun échec de requête pendant le test
-  Performance stable avec 6 utilisateurs simultanés

## Conclusion
L'application respecte toutes les exigences de performance :
- Liste compétitions : < 5 secondes 
- Mise à jour points : < 2 secondes 

