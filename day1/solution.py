import requests
import os

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
        # Parse the data - assuming it's a list of numbers separated by whitespace
        data = response.text.strip().split()
        # Convert to integers
        numbers = [int(x) for x in data if x.isdigit()]
        print(f"Retrieved {len(numbers)} numbers")
        return numbers
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

def sortedDistance(a, b):
    """Calculate sorted distance between two lists"""
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    print(f"List A sorted: {a_sorted}")
    print(f"List B sorted: {b_sorted}")
    distances = [abs(a_i - b_i) for (a_i, b_i) in zip(a_sorted, b_sorted)]
    print(f"Distances: {distances}")
    return sum(e for e in distances)

def main():
    print("Advent of Code 2024 - Day 1 Solution")
    print("=" * 40)
    
    # Get data from Advent of Code
    advent_data = get_advent_of_code_data()
    
    if advent_data is None:
        print("Could not fetch data, using fallback data...")
        # Fallback to original hardcoded data
        a = [3, 4, 2, 1, 3, 3]
        b = [4, 3, 5, 3, 9, 3]
    else:
        # Split the data into two lists for the algorithm
        # For this example, we'll split the data in half
        mid_point = len(advent_data) // 2
        a = advent_data[:mid_point]
        b = advent_data[mid_point:]
        print(f"Using first {len(a)} numbers as list A")
        print(f"Using last {len(b)} numbers as list B")
    
    print(f"\nList A: {a}")
    print(f"List B: {b}")
    
    # Calculate sorted distance
    result = sortedDistance(a, b)
    print(f"\nResult: {result}")

if __name__ == "__main__":
    main()
