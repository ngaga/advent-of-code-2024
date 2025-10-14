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


def read_string(corrupted_memory, string_to_read, current_index):
    return corrupted_memory[current_index:current_index+len(string_to_read)].startswith(string_to_read)

# Reads a int number which is up to 3 digits long.
# returns (number or None, the next index to start searching for next pattern)
def read_number(corrupted_memory, current_index):
    i = current_index
    # Find the start of the number (skip non-digit characters)
    while i < len(corrupted_memory) and not corrupted_memory[i].isdigit():
        i += 1
    
    if i >= len(corrupted_memory):
        return (None, i)
    
    # Read up to 3 digits
    number_str = ""
    max_digits = min(3, len(corrupted_memory) - i)
    for j in range(max_digits):
        if corrupted_memory[i + j].isdigit():
            number_str += corrupted_memory[i + j]
        else:
            break
    
    if number_str:
        number = int(number_str)
        if 1 <= number <= 999:  # Numbers must be 1-3 digits
            return (number, i + len(number_str))
    
    return (None, i + 1)

def find_valid_mul_instructions(corrupted_memory):
    """Find all valid mul instructions in the corrupted memory.
    
    Valid mul instructions must:
    - Start with 'mul('
    - Have two numbers separated by comma
    - End with ')'
    - Numbers must be 1-3 digits
    """
    valid_instructions = []
    i = 0
    while i < len(corrupted_memory):
        if read_string(corrupted_memory, "mul(", i):
            # Move past "mul(" (4 characters)
            i += 4
            first_number_result, i = read_number(corrupted_memory, i)
            if first_number_result is not None:
                # Look for comma
                if i < len(corrupted_memory) and corrupted_memory[i] == ',':
                    i += 1  # Move past comma
                    second_number_result, i = read_number(corrupted_memory, i)
                    if second_number_result is not None:
                        # Look for closing parenthesis
                        if i < len(corrupted_memory) and corrupted_memory[i] == ')':
                            valid_instructions.append((first_number_result, second_number_result))
                            i += 1  # Move past closing parenthesis
                        else:
                            i += 1  # Move forward if no closing parenthesis
                    else:
                        i += 1  # Move forward if second number not found
                else:
                    i += 1  # Move forward if no comma found
            else:
                i += 1  # Move forward if first number not found
        else:
            i += 1  # Move forward if "mul(" not found
    return valid_instructions

# pass a list of pairs of numbers
def calculate_multiplication_sum(instructions):
    return sum(instruction[0] * instruction[1] for instruction in instructions)

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
    valid_instructions = find_valid_mul_instructions(corrupted_memory)
    print(f"Found {len(valid_instructions)} valid mul instructions")
    print(f"Valid instructions: {valid_instructions}")
    total_sum = calculate_multiplication_sum(valid_instructions)
    print(f"Sum of all valid mul instruction results: {total_sum}")

if __name__ == "__main__":
    main()
