#!/usr/bin/env python3
"""
Advent of Code 2024 - Day 3 Solution
"""

import requests
import os
import re

def get_advent_of_code_data():
    """Fetch data from Advent of Code 2024 Day 3"""
    url = "https://adventofcode.com/2024/day/3/input"
    # Get session from environment variable
    my_session = os.getenv('ADVENT_OF_CODE_SESSION')
    if not my_session:
        raise ValueError("ADVENT_OF_CODE_SESSION environment variable not set. Please check your .env file.")
    cookies = {'session': my_session}
    
    print("Fetching data from Advent of Code...")
    response = requests.get(url, cookies=cookies)
    
    if response.status_code == 200:
        print("Data fetched successfully!")
        # Parse the data - corrupted memory as a single string
        corrupted_memory = response.text.strip()
        
        print(f"Retrieved corrupted memory of length {len(corrupted_memory)}")
        return corrupted_memory
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

def find_valid_mul_instructions(corrupted_memory):
    """Find all valid mul instructions in the corrupted memory.
    
    Valid mul instructions must:
    - Start with 'mul('
    - Have two numbers separated by comma
    - End with ')'
    - Numbers must be 1-3 digits
    """
    # TODO: Implement the algorithm to find valid mul instructions
    # This is where you'll implement the parsing logic
    pass

def calculate_multiplication_sum(corrupted_memory):
    """Calculate the sum of all valid mul instruction results.
    
    Returns the sum of all multiplication results from valid mul instructions.
    """
    # TODO: Implement the calculation logic
    # This is where you'll implement the calculation
    pass

def main():
    print("Advent of Code 2024 - Day 3 Solution")
    print("=" * 40)
    
    # Get data from Advent of Code
    corrupted_memory = get_advent_of_code_data()
    
    if corrupted_memory is None:
        print("Error: Failed to fetch data from Advent of Code")
        return
    
    print(f"Loaded corrupted memory of length {len(corrupted_memory)}")
    
    # Calculate the sum of all valid mul instructions
    total_sum = calculate_multiplication_sum(corrupted_memory)
    print(f"Sum of all valid mul instruction results: {total_sum}")

if __name__ == "__main__":
    main()
