import requests
import os
import numpy as np

def get_advent_of_code_data():
    """Fetch data from Advent of Code 2024 Day 1"""
    url = "https://adventofcode.com/2024/day/1/input"
    # Get session from environment variable
    my_session = os.getenv('ADVENT_OF_CODE_SESSION')
    if not my_session:
        raise ValueError("ADVENT_OF_CODE_SESSION environment variable not set. Please check your .env file.")
    cookies = {'session': my_session}
    
    print("Fetching data from Advent of Code...")
    response = requests.get(url, cookies=cookies)
    
    if response.status_code == 200:
        print("Data fetched successfully!")
        # Parse the data - each line contains two numbers separated by whitespace
        lines = response.text.strip().split('\n')
        
        # Filter valid lines and count them
        valid_lines = [line for line in lines if line.strip() and len(line.split()) == 2]
        num_pairs = len(valid_lines)
        
        if num_pairs == 0:
            print("No valid data found")
            return None
        
        # Create matrix directly
        matrix = np.zeros((num_pairs, 2), dtype=int)
        for i, line in enumerate(valid_lines):
            numbers = line.split()
            matrix[i, 0] = int(numbers[0])
            matrix[i, 1] = int(numbers[1])
        
        print(f"Retrieved {num_pairs} pairs of numbers")
        print(f"Matrix shape: {matrix.shape}")
        return matrix
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

def calculate_sorted_distance(matrix):
    """Calculate sorted distance between the two columns of the matrix"""
    # Extract columns
    col_a = matrix[:, 0]  # First column
    col_b = matrix[:, 1]  # Second column
    
    # Sort both columns
    col_a_sorted = np.sort(col_a)
    col_b_sorted = np.sort(col_b)
    
    print(f"Column A sorted: {col_a_sorted}")
    print(f"Column B sorted: {col_b_sorted}")
    
    # Calculate absolute differences
    distances = np.abs(col_a_sorted - col_b_sorted)
    print(f"Distances: {distances}")
    
    return np.sum(distances)

def main():
    print("Advent of Code 2024 - Day 1 Solution")
    print("=" * 40)
    
    # Get data from Advent of Code
    matrix = get_advent_of_code_data()
    
    if matrix is None:
        print("Error: Failed to fetch data from Advent of Code")
        return
    else:
        print(f"\nMatrix:")
        print(matrix)
        print(f"Shape: {matrix.shape}")
        
        # Calculate sorted distance between the two columns
        result = calculate_sorted_distance(matrix)
        print(f"\nResult: {result}")

if __name__ == "__main__":
    main()
