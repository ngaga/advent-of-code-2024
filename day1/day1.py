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
    """Fetch data from Advent of Code 2024 Day 1"""
    url = "https://adventofcode.com/2024/day/1/input"
    # Get session from environment variable
    my_session = os.getenv('ADVENT_OF_CODE_SESSION')
    if not my_session:
        raise ValueError("ADVENT_OF_CODE_SESSION environment variable not set. Please check your .env file.")
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

# Count how many times each number of the leftList is present in the rightList and add this number 
# multiplied by the number of the leftList to the result.
# complexity is O(n^2) where n is the length of the longest list -> we can do better probably.
def brute_force_calculate_similarity_index(leftList, rightList):
    result = 0
    for l in leftList:
        count = rightList.count(l)
        result += l * count
    return result


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
      
        sorted_distance = distanceSumOfSortedElements(col_a.tolist(), col_b.tolist())
        similarity_index = brute_force_calculate_similarity_index(col_a.tolist(), col_b.tolist())
        
        logger.success(f"Part 1: {sorted_distance}")
        logger.success(f"Part 2: {similarity_index}")

if __name__ == "__main__":
    main()
