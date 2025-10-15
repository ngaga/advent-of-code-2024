#!/bin/bash

# Script to easily run the Advent of Code 2024 project with Docker

echo "Advent of Code 2024 - Docker Runner"
echo "======================================"

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "Building Docker image (no cache)..."
docker-compose build --no-cache

echo ""
echo "Running all tests..."
echo "===================="
echo "=== Day 1 Tests ==="
docker-compose run --rm advent-of-code python -m pytest day1/test_day1.py -v
echo ""
echo "=== Day 2 Tests ==="
docker-compose run --rm advent-of-code python -m pytest day2/test_day2.py -v
echo ""
echo "=== Day 3 Tests ==="
docker-compose run --rm advent-of-code python -m pytest day3/test_day3.py -v
echo ""
echo "=== Day 4 Tests ==="
docker-compose run --rm advent-of-code python -m pytest day4/test_day4.py -v

echo ""
echo "Running all solutions..."
echo "======================="
echo "=== Day 1 Solution ==="
docker-compose run --rm advent-of-code python day1/day1.py
echo ""
echo "=== Day 2 Solution ==="
docker-compose run --rm advent-of-code python day2/day2.py
echo ""
echo "=== Day 3 Solution ==="
docker-compose run --rm advent-of-code python day3/day3.py
echo ""
echo "=== Day 4 Solution ==="
docker-compose run --rm advent-of-code python day4/day4.py

echo ""
echo "Done!"