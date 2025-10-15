#!/usr/bin/env python3
"""
Advent of Code 2024 - Day 4 Solution
"""

import requests
import os
import numpy as np
import sys

# Add parent directory to path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.common_logger import setup_logger, get_logger

# Setup logger
setup_logger()
logger = get_logger()

def get_advent_of_code_data():
    """Fetch data from Advent of Code 2024 Day 4"""
    url = "https://adventofcode.com/2024/day/4/input"
    # Get session from environment variable
    my_session = os.getenv('ADVENT_OF_CODE_SESSION')
    if not my_session:
        raise ValueError("ADVENT_OF_CODE_SESSION environment variable not set. Please check your .env file.")
    cookies = {'session': my_session}
    
    logger.debug("Fetching data from Advent of Code...")
    response = requests.get(url, cookies=cookies)
    
    if response.status_code == 200:
        logger.debug("Data fetched successfully!")
        # Parse the data - each line is a row of the word search grid
        lines = response.text.strip().split('\n')
        
        # Filter valid lines (non-empty)
        grid = [line.strip() for line in lines if line.strip()]
        
        if not grid:
            logger.warning("No valid data found")
            return None
        
        logger.debug(f"Retrieved word search grid of size {len(grid)}x{len(grid[0]) if grid else 0}")
        return grid
    else:
        logger.error(f"Error fetching data: {response.status_code}")
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

def find_x_mas_patterns(grid):
    """Find all X-MAS patterns in the grid using convolution"""
    # Handle empty grid
    if not grid or not grid[0]:
        return []
    
    # Convert grid to numpy array - ensure all rows have same length
    max_len = max(len(row) for row in grid)
    padded_grid = [row.ljust(max_len) for row in grid]
    grid_array = np.array([list(row) for row in padded_grid])
    rows, cols = grid_array.shape
    
    # Define all possible X-MAS convolution kernels
    # Each kernel is a 3x3 pattern with the center being 'A'
    # Only X-shaped patterns (not +-shaped)
    kernels = [
        # Pattern 1: 2M en haut, 2S en bas
        np.array([['M', '.', 'M'],
                  ['.', 'A', '.'],
                  ['S', '.', 'S']]),
        
        # Pattern 2: 2M en bas, 2S en haut
        np.array([['S', '.', 'S'],
                  ['.', 'A', '.'],
                  ['M', '.', 'M']]),
        
        # Pattern 3: 2M à gauche, 2S à droite
        np.array([['M', '.', 'S'],
                  ['.', 'A', '.'],
                  ['M', '.', 'S']]),
        
        # Pattern 4: 2M à droite, 2S à gauche
        np.array([['S', '.', 'M'],
                  ['.', 'A', '.'],
                  ['S', '.', 'M']]),
    ]
    
    occurrences = []
    
    # Check each position in the grid (except edges)
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            # Extract 3x3 subgrid centered at (row, col)
            subgrid = grid_array[row-1:row+2, col-1:col+2]
            
            # Check against each kernel
            for kernel in kernels:
                # Check if subgrid matches kernel
                # We need to handle the case where kernel has '.' (any character)
                match = True
                for i in range(3):
                    for j in range(3):
                        if kernel[i, j] != '.' and subgrid[i, j] != kernel[i, j]:
                            match = False
                            break
                    if not match:
                        break
                
                if match:
                    occurrences.append((row, col, kernel))
                    break  # Found a match, no need to check other kernels
    
    return occurrences

def count_x_mas_in_grid(grid):
    """Count total number of X-MAS patterns in the grid"""
    occurrences = find_x_mas_patterns(grid)
    return len(occurrences)

def main():
    
    # Get data from Advent of Code
    grid = get_advent_of_code_data()
    
    if grid is None:
        logger.error("Error: Failed to fetch data from Advent of Code")
        return  
    
    logger.success(f"Part 1: {count_xmas_in_grid(grid)}")
    logger.success(f"Part 2: {count_x_mas_in_grid(grid)}")

if __name__ == "__main__":
    main()
    