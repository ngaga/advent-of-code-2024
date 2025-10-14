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
    # Check if we have enough characters and if the substring matches
    if current_index + len(string_to_read) > len(corrupted_memory):
        return (False, current_index + 1)
    if corrupted_memory[current_index:current_index+len(string_to_read)] == string_to_read:
        return (True, current_index + len(string_to_read))
    return (False, current_index + 1)

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
        if 0 <= number <= 999:  # Numbers must be 0-3 digits
            return (number, i + len(number_str))
    
    return (None, i + 4)

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
        found, i = read_string(corrupted_memory, "mul(", i)
        if found:
            first_number_result, i = read_number(corrupted_memory, i)
            if first_number_result is not None:
                found_comma, i = read_string(corrupted_memory, ",", i)
                if found_comma:
                    second_number_result, i = read_number(corrupted_memory, i)
                    if second_number_result is not None:
                        found_parenthesis, i = read_string(corrupted_memory, ")", i)
                        if found_parenthesis:
                            valid_instructions.append((first_number_result, second_number_result))
    return valid_instructions

# pass a list of pairs of numbers
def calculate_multiplication_sum(instructions):
    return sum(instruction[0] * instruction[1] for instruction in instructions)

# Returns the string curated from what is in between a "don't()" and a "do()" keywords
# We are in a "do()" state at the beginning.
# Add to the current character to the result string while we are in a do state
def extract_do_instructions(corrupted_memory):
    result = ""
    i = 0
    do_state = True
    while i < len(corrupted_memory):
        if do_state:
            # look for "don't()" in the input string
            found, new_i = read_string(corrupted_memory, "don't()", i)
            if found:
                do_state = False
                i = new_i
            else:
                # Add current character to result (before read_string advanced)
                if i < len(corrupted_memory):
                    result += corrupted_memory[i]
                i = new_i
        else:
            # look for "do()" in the input string
            found, i = read_string(corrupted_memory, "do()", i)
            if found:
                do_state = True
            else:
                # Do not happen anything because we are in a "don't()" state
                pass
    return result


def main():
    print("Advent of Code 2024 - Day 3 Solution")
    print("=" * 40)
    
    # Get data from Advent of Code
    corrupted_memory = get_advent_of_code_data()
    
    if corrupted_memory is None:
        print("Error: Failed to fetch data from Advent of Code")
        return
    
    print(f"Loaded corrupted memory of length {len(corrupted_memory)}")
    
    # Part 1: Calculate the sum of all valid mul instructions
    valid_instructions = find_valid_mul_instructions(corrupted_memory)
    print(f"Part 1 - Found {len(valid_instructions)} valid mul instructions")
    print(f"Valid instructions: {valid_instructions}")
    total_sum = calculate_multiplication_sum(valid_instructions)
    print(f"Part 1 - Sum of all valid mul instruction results: {total_sum}")
    
    # Part 2: Calculate the sum considering do() and dont() state
    print("\n" + "=" * 40)
    print("Part 2 - With do() and dont() state management")
    print("=" * 40)
    
    do_instructions = extract_do_instructions(corrupted_memory)
    print(f"Part 2 - Do instructions: {do_instructions}")
    total_sum_part2 = calculate_multiplication_sum(find_valid_mul_instructions(do_instructions))
    print(f"Part 2 - Sum of all valid mul instruction results: {total_sum_part2}")

if __name__ == "__main__":
    main()
