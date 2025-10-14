#!/usr/bin/env python3
"""
Advent of Code 2024 - Day 4 Solution
"""

import requests
import os
import numpy as np

def get_advent_of_code_data():
    """Fetch data from Advent of Code 2024 Day 4"""
    url = "https://adventofcode.com/2024/day/4/input"
    # Get session from environment variable
    my_session = os.getenv('ADVENT_OF_CODE_SESSION')
    if not my_session:
        raise ValueError("ADVENT_OF_CODE_SESSION environment variable not set. Please check your .env file.")
    cookies = {'session': my_session}
    
    print("Fetching data from Advent of Code...")
    response = requests.get(url, cookies=cookies)
    
    if response.status_code == 200:
        print("Data fetched successfully!")
        # Parse the data - each line is a row of the word search grid
        lines = response.text.strip().split('\n')
        
        # Filter valid lines (non-empty)
        grid = [line.strip() for line in lines if line.strip()]
        
        if not grid:
            print("No valid data found")
            return None
        
        print(f"Retrieved word search grid of size {len(grid)}x{len(grid[0]) if grid else 0}")
        return grid
    else:
        print(f"Error fetching data: {response.status_code}")
        return None
    

def find_xmas_occurrences(grid):
    """Find all XMAS occurrences in the grid"""
    # Handle empty grid
    if not grid or not grid[0]:
        return []
    
    # Convert grid to numpy array - ensure all rows have same length
    max_len = max(len(row) for row in grid)
    padded_grid = [row.ljust(max_len) for row in grid]
    grid_array = np.array([list(row) for row in padded_grid])
    rows, cols = grid_array.shape
    
    # Define the 8 directions: (row_delta, col_delta)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # Up-left, Up, Up-right
        (0, -1),           (0, 1),   # Left, Right
        (1, -1),  (1, 0),  (1, 1)    # Down-left, Down, Down-right
    ]
    
    # Target word
    target = "XMAS"
    
    occurrences = []
    
    # Check each position in the grid
    for row in range(rows):
        for col in range(cols):
            # Check each direction from this position
            for dr, dc in directions:
                # Check if we can fit the word in this direction
                end_row = row + (len(target) - 1) * dr
                end_col = col + (len(target) - 1) * dc
                
                # Check bounds
                if 0 <= end_row < rows and 0 <= end_col < cols:
                    # Extract the word in this direction
                    word = ""
                    for i in range(len(target)):
                        word += grid_array[row + i * dr, col + i * dc]
                    
                    # Check if it matches XMAS
                    if word == target:
                        occurrences.append((row, col, dr, dc, word))
    
    return occurrences

def count_xmas_in_grid(grid):
    """Count total number of XMAS occurrences in the grid"""
    occurrences = find_xmas_occurrences(grid)
    return len(occurrences)

def main():
    print("Advent of Code 2024 - Day 4 Solution")
    print("=" * 40)
    
    # Get data from Advent of Code
    grid = get_advent_of_code_data()
    
    if grid is None:
        print("Error: Failed to fetch data from Advent of Code")
        return  
    
    print(f"Number of XMAS occurrences: {count_xmas_in_grid(grid)}")

if __name__ == "__main__":
    main()
    