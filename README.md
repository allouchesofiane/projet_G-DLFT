# GÜDLFT Registration Platform

##  Description
Application légère de réservation pour compétitions de force (deadlifting, strongman) destinée aux organisateurs régionaux.

Permet aux secrétaires de clubs d'inscrire des athlètes aux compétitions en utilisant un système de points.

##  Fonctionnalités

### Phase 1
-  Connexion par email (secrétaires de clubs)
-  Affichage des compétitions à venir
-  Réservation de places avec système de points (1 point = 1 place)
-  Déduction automatique des points
-  Limite de 12 places max par compétition et par club
-  Validation : points suffisants + compétitions futures uniquement
-  Messages de confirmation et d'erreur

### Phase 2
-  Tableau public des points de tous les clubs
-  Accessible sans connexion
-  Lecture seule
-  Tri par points décroissants

##  Bugs corrigés
1.  **Email inexistant fait planter l'app** (bug critique ligne 29)
2.  **Points non déduits** après réservation
3.  **Réservation pour compétitions passées** possible
4.  **Pas de limite à 12 places** par compétition
5.  **Overspending de points** possible

##  Installation

### Prérequis
- Python 3.8+
- pip

### Étapes

1. **Cloner le repository**
```bash
git clone https://github.com/OpenClassrooms-Student-Center/Python_Testing.git
cd Python_Testing
```

2. **Créer l'environnement virtuel**
```bash
python -m venv env
```

3. **Activer l'environnement virtuel**
- Windows : `env\Scripts\activate`
- macOS/Linux : `source env/bin/activate`

4. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

5. **Lancer l'application**
```bash
python server.py
```

6. **Ouvrir dans le navigateur**
```
http://127.0.0.1:5000/
```

##  Tests

### Lancer tous les tests
```bash
pytest
```

### Avec rapport de couverture
```bash
pytest --cov=. --cov-report=html --cov-report=term
```

### Tests par catégorie
```bash
# Tests unitaires
pytest tests/unit/

# Tests d'intégration
pytest tests/integration/

# Tests fonctionnels
pytest tests/functional/
```

### Couverture de code
- **Couverture actuelle** : 72% ✅ (≥ 60% requis)
- **Rapport HTML** : `htmlcov/index.html`

### Tests de performance
```bash
# Lancer le serveur
python server.py

# Dans un autre terminal, lancer Locust
locust

# Ouvrir http://localhost:8089
# Configuration : 6 utilisateurs, spawn rate 1/s
```

##  Structure du projet
```
Python_Testing/
├── server.py                   # Application Flask principale
├── clubs.json                  # Données des clubs
├── competitions.json           # Données des compétitions
├── templates/                  # Templates HTML
│   ├── index.html             # Page d'accueil
│   ├── welcome.html           # Liste compétitions
│   ├── booking.html           # Formulaire réservation
│   └── points.html            # Tableau public (Phase 2)
├── tests/                      # Tests
│   ├── unit/                  # Tests unitaires
│   ├── integration/           # Tests d'intégration
│   ├── functional/            # Tests fonctionnels
│   └── conftest.py            # Fixtures pytest
├── locustfile.py              # Tests de performance
├── pytest.ini                 # Configuration pytest
├── .coveragerc                # Configuration coverage
├── requirements.txt           # Dépendances Python
├── TEST_REPORT.md            # Rapport de tests
├── PERFORMANCE_REPORT.md     # Rapport de performance
├── BUGS.md                    # Suivi des bugs
└── README.md                  # Ce fichier
```

##  Workflow Git

### Nomenclature des branches
- `main` : Branche principale (code stable)
- `bug/*` : Correction de bugs (ex: `bug/email-not-found-crash`)
- `feature/*` : Nouvelles fonctionnalités (ex: `feature/public-points-board`)
- `qa` : Branche de révision (quality assurance)

### Exemple
```bash
# Créer une branche pour un bug
git checkout -b bug/nom-du-bug

# Merger dans main si tests OK
git checkout main
git merge bug/nom-du-bug
```

##  Performance

### Exigences
-  Chargement liste compétitions : < 5 secondes
-  Mise à jour points : < 2 secondes
-  Tests avec 6 utilisateurs simultanés

### Résultats
Voir `PERFORMANCE_REPORT.md` pour les résultats détaillés.

##  Règles métier

1. **Système de points**
   - 1 point = 1 place
   - Les clubs gagnent des points en organisant des compétitions

2. **Limitations**
   - Maximum 12 places par club et par compétition
   - Ne peut pas dépenser plus de points que disponible
   - Ne peut pas réserver pour une compétition passée
   - Ne peut pas réserver plus de places que disponibles

3. **Accès**
   - Seuls les secrétaires peuvent réserver (authentification par email)
   - Tableau public accessible à tous sans connexion

##  Documentation

- **Tests** : [TEST_REPORT.md](./TEST_REPORT.md)
- **Performance** : [PERFORMANCE_REPORT.md](./PERFORMANCE_REPORT.md)
- **Bugs** : [BUGS.md](./BUGS.md)

##  Auteur
Sofiane ALLOUCHE

##  Licence
Ce projet est développé dans la cadre d'une formation avec OpenClassrooms