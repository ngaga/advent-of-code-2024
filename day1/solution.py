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

def sort_lists(list_a, list_b):
    """Sort two lists and return the sorted versions"""
    return sorted(list_a), sorted(list_b)

def calculate_similarity_index(sorted_list_a, sorted_list_b):
    """Calculate similarity index between two sorted lists"""
    # Day 1 part 2
    # We benefit from the fact that the columns are sorted already.
    # If the values are different, the multiplier will be 0 so no need to add anything.
    # If the values are the same, we add the value to the result. And it will be the same 
    # for each further matching value. So if we have 3 times 3 we will correcly add 9.
    i = 0
    j = 0
    result = 0
    while i < len(sorted_list_a) and j < len(sorted_list_b):
        if sorted_list_a[i] < sorted_list_b[j]:
            i += 1
        elif sorted_list_a[i] > sorted_list_b[j]:
            j += 1
        else: # sorted_list_a[i] == sorted_list_b[j]
            result += sorted_list_a[i]
            i += 1
            j += 1
    
    return result

def sortedDistance(list_a, list_b):
    """Calculate sorted distance between two lists (for testing purposes)"""
    # Sort both lists
    sorted_a, sorted_b = sort_lists(list_a, list_b)
    
    # Calculate absolute differences
    distances = [abs(a - b) for a, b in zip(sorted_a, sorted_b)]
    
    return sum(distances)


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
        
        # Extract columns
        col_a = matrix[:, 0]  # First column
        col_b = matrix[:, 1]  # Second column
        
        # Sort both columns
        col_a_sorted = np.sort(col_a)
        col_b_sorted = np.sort(col_b)
        
        print(f"Column A sorted: {col_a_sorted}")
        print(f"Column B sorted: {col_b_sorted}")
        
        # Calculate sorted distance using the sortedDistance function
        sorted_distance = sortedDistance(col_a.tolist(), col_b.tolist())
        print(f"Sorted distance: {sorted_distance}")
        
        # Calculate similarity index
        similarity_index = calculate_similarity_index(col_a_sorted, col_b_sorted)
        print(f"Similarity index: {similarity_index}")
        
        print(f"\nResults:")
        print(f"Sorted distance: {sorted_distance}")
        print(f"Similarity index: {similarity_index}")

if __name__ == "__main__":
    main()
