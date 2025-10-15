import requests
import os
import numpy as np
from collections import Counter

from utils.common_logger import setup_logger, get_logger

# Setup logger
setup_logger()
logger = get_logger()

def get_advent_of_code_data():
    """Fetch data from Advent of Code 2024 Day 1"""
    url = "https://adventofcode.com/2024/day/1/input"
    # Get session from environment variable
    my_session = os.getenv('ADVENT_OF_CODE_SESSION')
    if not my_session:
        logger.error("ADVENT_OF_CODE_SESSION environment variable not set. Please create or modify the .env as explained in the README.md. Skipping solution execution for now.")
        return None
    cookies = {'session': my_session}
    
    logger.debug("Fetching data from Advent of Code...")
    response = requests.get(url, cookies=cookies)
    
    if response.status_code == 200:
        logger.debug("Data fetched successfully!")
        # Parse the data - each line contains two numbers separated by whitespace
        lines = response.text.strip().split('\n')
        
        # Filter valid lines and count them
        valid_lines = [line for line in lines if line.strip() and len(line.split()) == 2]
        num_pairs = len(valid_lines)
        
        if num_pairs == 0:
            logger.warning("No valid data found")
            return None
        
        # Create matrix directly
        matrix = np.zeros((num_pairs, 2), dtype=int)
        for i, line in enumerate(valid_lines):
            numbers = line.split()
            matrix[i, 0] = int(numbers[0])
            matrix[i, 1] = int(numbers[1])
        
        return matrix
    else:
        logger.error(f"Error fetching data: {response.status_code}")
        return None


# Count occurrences in the right list: O(n)
# Calculate the score: O(n)
# Complexity: O(n)
def similarity_score(left_list, right_list):
    right_counter = Counter(right_list) 
    return sum(item * right_counter[item] for item in left_list)


def distanceSumOfSortedElements(list_a, list_b):
    sorted_a, sorted_b = sorted(list_a), sorted(list_b)
    distances = [abs(a - b) for a, b in zip(sorted_a, sorted_b)]
    return sum(distances)


def main():
    
    # Get data from Advent of Code
    matrix = get_advent_of_code_data()

    if matrix is None:
        logger.error("Error: Failed to fetch data from Advent of Code")
        return
    else:
        # Extract columns
        col_a = matrix[:, 0]  # First column
        col_b = matrix[:, 1]  # Second column
        # TODO: numpy matrix finally not needed here. Could be replaced by lists.
        sorted_distance = distanceSumOfSortedElements(col_a.tolist(), col_b.tolist())
        similarity_index = similarity_score(col_a.tolist(), col_b.tolist())
        
        logger.success(f"Part 1: {sorted_distance}")
        logger.success(f"Part 2: {similarity_index}")

if __name__ == "__main__":
    main()
