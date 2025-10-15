#!/usr/bin/env python3
"""
Advent of Code 2024 - Day 2 Solution
"""

import requests
import os
import sys

# Add parent directory to path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.common_logger import setup_logger, get_logger

# Setup logger
setup_logger()
logger = get_logger()

def get_advent_of_code_data():
    """Fetch data from Advent of Code 2024 Day 2"""
    url = "https://adventofcode.com/2024/day/2/input"
    # Get session from environment variable
    my_session = os.getenv('ADVENT_OF_CODE_SESSION')
    if not my_session:
        raise ValueError("ADVENT_OF_CODE_SESSION environment variable not set. Please check your .env file.")
    cookies = {'session': my_session}
    
    logger.debug("Fetching data from Advent of Code...")
    response = requests.get(url, cookies=cookies)
    
    if response.status_code == 200:
        logger.debug("Data fetched successfully!")
        # Parse the data - each line contains numbers separated by whitespace
        lines = response.text.strip().split('\n')
        
        # Filter valid lines and convert to integers
        reports = []
        for line in lines:
            if line.strip():  # Skip empty lines
                report = [int(x) for x in line.strip().split()]
                reports.append(report)
        
        logger.debug(f"Retrieved {len(reports)} reports")
        return reports
    else:
        logger.error(f"Error fetching data: {response.status_code}")
        return None

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

def is_safe_by_one_report(report):
    """Check if a report is safe according to the rules with Problem Dampener:
    - Try removing each element and see if any resulting report is safe
    - If the original report is already safe, return True
    """
    # Single value or empty report is considered safe
    if len(report) < 2:
        return True
    
    # Check if the original report is already safe
    if is_safe_report(report):
        return True
    
    # Try removing each element and check if the resulting report is safe
    for i in range(len(report)):
        # Create a new report without the element at index i
        modified_report = report[:i] + report[i+1:]
        if is_safe_report(modified_report):
            return True
    
    return False

def count_safe_reports(reports):
    # A report is safe if:
    # 1. All levels are either increasing or decreasing
    # 2. Any two adjacent levels differ by at least 1 and at most 3
    safe_count = 0
    for report in reports:
        if is_safe_report(report):
            safe_count += 1
    return safe_count

def count_safe_reports_by_one_report(reports):
    safe_count = 0
    for report in reports:
        if is_safe_by_one_report(report):
            safe_count += 1
    return safe_count

def main():
    
    # Get data from Advent of Code
    reports = get_advent_of_code_data()
    
    if reports is None:
        logger.error("Error: Failed to fetch data from Advent of Code")
        return
    
    
    # Count safe reports
    safe_count = count_safe_reports(reports)
    safe_count_by_one_report = count_safe_reports_by_one_report(reports)
    
    logger.success(f"Part 1: {safe_count} out of {len(reports)}")
    logger.success(f"Part 2: {safe_count_by_one_report} out of {len(reports)}")

if __name__ == "__main__":
    main()
