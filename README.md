# Advent of Code 2024

Mes solutions pour l'Advent of Code 2024.

## 🐳 Installation et exécution avec Docker

### Prérequis
- Docker
- Docker Compose

### Lancement rapide

#### Option 1: Script automatique (recommandé)
```bash
./run.sh
```

#### Option 2: Commandes Docker manuelles

**Construire l'image :**
```bash
docker-compose build
```

**Exécuter une solution spécifique :**
```bash
# Jour 1
docker-compose run --rm advent-of-code python day1/solution.py

# Jour 2
docker-compose run --rm advent-of-code python day2/solution.py

# Jour 3
docker-compose run --rm advent-of-code python day3/solution.py

# Jour 4
docker-compose run --rm advent-of-code python day4/solution.py
```

**Exécuter les tests :**
```bash
# Tests d'un jour spécifique
docker-compose run --rm advent-of-code python -m pytest day1/test_solution.py -v

# Tests de tous les jours
docker-compose run --rm advent-of-code python -m pytest day*/test_solution.py -v
```

### Structure du projet
```
├── day1/
│   ├── solution.py                    # Solution du jour 1
│   ├── test_solution.py              # Tests du jour 1
│   └── test_connection.py            # Test de connexion
├── day2/
│   ├── solution.py                    # Solution du jour 2
│   └── test_solution.py              # Tests du jour 2
├── day3/
│   ├── solution.py                    # Solution du jour 3
│   └── test_solution.py              # Tests du jour 3
├── day4/
│   ├── solution.py                    # Solution du jour 4
│   └── test_solution.py              # Tests du jour 4
├── Dockerfile                         # Configuration Docker
├── docker-compose.yml                # Configuration Docker Compose
├── requirements.txt                   # Dépendances Python
├── run.sh                           # Script d'aide pour l'exécution
└── README.md                        # Ce fichier
```

### Dépendances
- Python 3.11
- requests==2.31.0

## 🚀 Installation locale (sans Docker)

Si vous préférez installer localement :

```bash
pip install -r requirements.txt
python day1/day_1_list_distances_sum.py
python day1/test_connection.py
```
