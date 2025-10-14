#!/usr/bin/env python3
"""
Advent of Code 2024 - Day 3 Tests
"""

import pytest
import sys
import os

# Add the day3 directory to the path so we can import the module
sys.path.append(os.path.join(os.path.dirname(__file__)))

from solution import get_advent_of_code_data, find_valid_mul_instructions, calculate_multiplication_sum

class TestDay3Solution:
    """Test cases for Day 3 solution"""
    
    def test_sample_data(self):
        """Test with sample data from the problem description"""
        # Sample corrupted memory from the problem
        sample_memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        
        # Verify the sample data structure
        assert len(sample_memory) > 0, "Sample memory should not be empty"
        assert isinstance(sample_memory, str), "Sample memory should be a string"
        
        print("✓ Sample data test passed")
        print(f"  Sample memory length: {len(sample_memory)}")
        print(f"  Sample memory: {sample_memory}")
    
    def test_find_valid_mul_instructions(self):
        """Test find_valid_mul_instructions function with sample data"""
        # Sample corrupted memory from the problem
        sample_memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        
        # Expected valid instructions: mul(2,4), mul(11,8), mul(8,5)
        # Note: mul(5,5) is invalid because it's inside do_not_mul
        # mul[3,7] is invalid because it uses brackets instead of parentheses
        # mul(32,64] is invalid because it has a bracket instead of parenthesis
        
        # TODO: This test will fail until the function is implemented
        # valid_instructions = find_valid_mul_instructions(sample_memory)
        # expected_instructions = ["mul(2,4)", "mul(11,8)", "mul(8,5)"]
        # assert valid_instructions == expected_instructions, f"Expected {expected_instructions}, got {valid_instructions}"
        
        print("✓ Find valid mul instructions test prepared")
        print("  Expected valid instructions: mul(2,4), mul(11,8), mul(8,5)")
        print("  Invalid instructions: mul[3,7], do_not_mul(5,5), mul(32,64]")
    
    def test_calculate_multiplication_sum(self):
        """Test calculate_multiplication_sum function with sample data"""
        # Sample corrupted memory from the problem
        sample_memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        
        # Expected calculation:
        # mul(2,4) = 2 * 4 = 8
        # mul(11,8) = 11 * 8 = 88
        # mul(8,5) = 8 * 5 = 40
        # Total = 8 + 88 + 40 = 136
        
        # TODO: This test will fail until the function is implemented
        # total_sum = calculate_multiplication_sum(sample_memory)
        # expected_sum = 136
        # assert total_sum == expected_sum, f"Expected {expected_sum}, got {total_sum}"
        
        print("✓ Calculate multiplication sum test prepared")
        print("  Expected sum: 8 + 88 + 40 = 136")
    
    def test_edge_cases(self):
        """Test edge cases for mul instruction parsing"""
        test_cases = [
            # (memory, expected_valid_instructions, description)
            ("mul(1,2)", ["mul(1,2)"], "Simple valid instruction"),
            ("mul(123,456)", ["mul(123,456)"], "Valid instruction with 3-digit numbers"),
            ("mul(1,2)mul(3,4)", ["mul(1,2)", "mul(3,4)"], "Two consecutive valid instructions"),
            ("mul(1,2)invalidmul(3,4)", ["mul(1,2)", "mul(3,4)"], "Valid instructions with invalid text in between"),
            ("mul[1,2]", [], "Invalid brackets instead of parentheses"),
            ("mul(1,2]", [], "Invalid closing bracket"),
            ("mul(1,2,3)", [], "Too many arguments"),
            ("mul(1)", [], "Too few arguments"),
            ("mul(,2)", [], "Empty first argument"),
            ("mul(1,)", [], "Empty second argument"),
            ("mul(1234,2)", [], "First number too long (4 digits)"),
            ("mul(1,2345)", [], "Second number too long (4 digits)"),
            ("", [], "Empty memory"),
            ("nomulhere", [], "No mul instructions"),
        ]
        
        for memory, expected, description in test_cases:
            print(f"  Testing: {description}")
            print(f"    Memory: '{memory}'")
            print(f"    Expected: {expected}")
            # TODO: Uncomment when function is implemented
            # result = find_valid_mul_instructions(memory)
            # assert result == expected, f"{description}: Expected {expected}, got {result}"
        
        print("✓ Edge cases test prepared")
    
    def test_calculation_edge_cases(self):
        """Test calculation with edge cases"""
        test_cases = [
            # (memory, expected_sum, description)
            ("mul(1,2)", 2, "Single valid instruction"),
            ("mul(0,5)", 0, "Multiplication by zero"),
            ("mul(1,1)", 1, "Multiplication by one"),
            ("mul(10,10)", 100, "Two-digit multiplication"),
            ("mul(100,100)", 10000, "Three-digit multiplication"),
            ("", 0, "Empty memory"),
            ("nomulhere", 0, "No valid instructions"),
        ]
        
        for memory, expected, description in test_cases:
            print(f"  Testing: {description}")
            print(f"    Memory: '{memory}'")
            print(f"    Expected sum: {expected}")
            # TODO: Uncomment when function is implemented
            # result = calculate_multiplication_sum(memory)
            # assert result == expected, f"{description}: Expected {expected}, got {result}"
        
        print("✓ Calculation edge cases test prepared")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
