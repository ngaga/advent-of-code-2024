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

echo "Building Docker image..."
echo "Choose build option:"
echo "1) Quick build (use cache)"
echo "2) Full rebuild (no cache)"
read -p "Enter your choice (1-2, default 1): " build_choice

case $build_choice in
    2)
        echo "Full rebuild (no cache)..."
        docker-compose build --no-cache
        ;;
    *)
        echo "Quick build (using cache)..."
        docker-compose build
        ;;
esac

echo "Running the application..."
echo "Choose which day to run:"
echo "1) Day 1 (default)"
echo "2) Day 2"
echo "3) Day 3"
echo "4) Day 4"
echo "5) Run all tests"
echo "6) Run specific day tests"

read -p "Enter your choice (1-6): " choice

case $choice in
    1|"")
        echo "Running Day 1 solution..."
        docker-compose run --rm advent-of-code python day1/solution.py
        ;;
    2)
        echo "Running Day 2 solution..."
        docker-compose run --rm advent-of-code python day2/solution.py
        ;;
    3)
        echo "Running Day 3 solution..."
        docker-compose run --rm advent-of-code python day3/solution.py
        ;;
    4)
        echo "Running Day 4 solution..."
        docker-compose run --rm advent-of-code python day4/solution.py
        ;;
    5)
        echo "Running all tests..."
        echo "=== Day 1 Tests ==="
        docker-compose run --rm advent-of-code python -m pytest day1/test_solution.py -v
        echo ""
        echo "=== Day 2 Tests ==="
        docker-compose run --rm advent-of-code python -m pytest day2/test_day2.py -v
        echo ""
        echo "=== Day 3 Tests ==="
        docker-compose run --rm advent-of-code python -m pytest day3/test_day3.py -v
        echo ""
        echo "=== Day 4 Tests ==="
        docker-compose run --rm advent-of-code python -m pytest day4/test_day4.py -v
        ;;
    6)
        echo "Choose which day tests to run:"
        echo "1) Day 1 tests"
        echo "2) Day 2 tests"
        echo "3) Day 3 tests"
        echo "4) Day 4 tests"
        read -p "Enter day number (1-4): " day_choice
        case $day_choice in
            1)
                echo "Running Day 1 tests..."
                docker-compose run --rm advent-of-code python -m pytest day1/test_solution.py -v
                ;;
            2)
                echo "Running Day 2 tests..."
                docker-compose run --rm advent-of-code python -m pytest day2/test_day2.py -v
                ;;
            3)
                echo "Running Day 3 tests..."
                docker-compose run --rm advent-of-code python -m pytest day3/test_day3.py -v
                ;;
            4)
                echo "Running Day 4 tests..."
                docker-compose run --rm advent-of-code python -m pytest day4/test_day4.py -v
                ;;
            *)
                echo "Invalid day choice. Running Day 1 tests..."
                docker-compose run --rm advent-of-code python -m pytest day1/test_solution.py -v
                ;;
        esac
        ;;
    *)
        echo "Invalid choice. Running Day 1 solution..."
        docker-compose run --rm advent-of-code python day1/solution.py
        ;;
esac

echo "Done!"
