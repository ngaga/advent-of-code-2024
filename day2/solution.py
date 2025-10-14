#!/usr/bin/env python3
"""
Advent of Code 2024 - Day 2 Solution
"""

import requests
import os

def get_advent_of_code_data():
    """Fetch data from Advent of Code 2024 Day 2"""
    url = "https://adventofcode.com/2024/day/2/input"
    # Get session from environment variable
    my_session = os.getenv('ADVENT_OF_CODE_SESSION')
    if not my_session:
        raise ValueError("ADVENT_OF_CODE_SESSION environment variable not set. Please check your .env file.")
    cookies = {'session': my_session}
    
    print("Fetching data from Advent of Code...")
    response = requests.get(url, cookies=cookies)
    
    if response.status_code == 200:
        print("Data fetched successfully!")
        # Parse the data - each line contains numbers separated by whitespace
        lines = response.text.strip().split('\n')
        
        # Filter valid lines and convert to integers
        reports = []
        for line in lines:
            if line.strip():  # Skip empty lines
                report = [int(x) for x in line.strip().split()]
                reports.append(report)
        
        print(f"Retrieved {len(reports)} reports")
        return reports
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

def load_data(filename):
    """Load data from file and return list of reports (kept for backward compatibility)"""
    with open(filename, 'r') as file:
        reports = []
        for line in file:
            report = [int(x) for x in line.strip().split()]
            reports.append(report)
        return reports


def is_safe_report(report):
    """Check if a report is safe according to the rules:
    - All levels are either increasing or decreasing
    - Any two adjacent levels differ by at least 1 and at most 3
    """
    if len(report) < 2:
        return True  # Single value or empty report is considered safe
    
    # Check if sequence is monotonic (increasing or decreasing)
    is_increasing = all(report[i] <= report[i+1] for i in range(len(report)-1))
    is_decreasing = all(report[i] >= report[i+1] for i in range(len(report)-1))
    
    if not (is_increasing or is_decreasing):
        return False  # Not monotonic
    
    # Check adjacent differences are between 1 and 3
    for i in range(len(report) - 1):
        delta = abs(report[i] - report[i+1])
        if delta < 1 or delta > 3:
            return False
    
    return True

def count_safe_reports(reports):
    # A report is safe if:
    # 1. All levels are either increasing or decreasing
    # 2. Any two adjacent levels differ by at least 1 and at most 3
    safe_count = 0
    for report in reports:
        if is_safe_report(report):
            print(f"Safe report: {report}")
            safe_count += 1
    return safe_count

def main():
    print("Advent of Code 2024 - Day 2 Solution")
    print("=" * 40)
    
    # Get data from Advent of Code
    reports = get_advent_of_code_data()
    
    if reports is None:
        print("Error: Failed to fetch data from Advent of Code")
        return
    
    print(f"Loaded {len(reports)} reports")
    
    # Count safe reports
    safe_count = count_safe_reports(reports)
    print(f"Number of safe reports: {safe_count} out of {len(reports)}")

if __name__ == "__main__":
    main()
