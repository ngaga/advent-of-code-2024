# Advent of Code 2024

My solutions for Advent of Code 2024.
<img width="853" height="255" alt="Capture d’écran 2025-10-14 à 17 27 36" src="https://github.com/user-attachments/assets/1d9251f1-162a-43b8-9b7c-80af14a38277" />

## Installation and execution with Docker

### Prerequisites
- Docker
- Docker Compose

### Quick start

#### Option 1: Automatic script (recommended)
```bash
./run.sh
```

#### Option 2: Manual Docker commands

**Build the image:**
```bash
docker-compose build
```

**Run a specific solution:**
```bash
# Day 1
docker-compose run --rm advent-of-code python day1/solution.py

# Day 2
docker-compose run --rm advent-of-code python day2/solution.py

# Day 3
docker-compose run --rm advent-of-code python day3/solution.py

# Day 4
docker-compose run --rm advent-of-code python day4/solution.py
```

**Run tests:**
```bash
# Tests for a specific day
docker-compose run --rm advent-of-code python -m pytest day1/test_solution.py -v

# Tests for all days
docker-compose run --rm advent-of-code python -m pytest day*/test_solution.py -v
```