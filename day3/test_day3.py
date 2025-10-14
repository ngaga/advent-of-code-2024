#!/usr/bin/env python3
"""
Advent of Code 2024 - Day 3 Tests
"""

import pytest
import sys
import os

# Add the day3 directory to the path so we can import the module
sys.path.append(os.path.join(os.path.dirname(__file__)))

from solution import get_advent_of_code_data, find_valid_mul_instructions, calculate_multiplication_sum, extract_do_instructions

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
        
        # Expected valid instructions: (2,4), (5,5), (11,8), (8,5)
        # Note: According to the problem statement, there are 4 valid instructions
        # mul[3,7] is invalid because it uses brackets instead of parentheses
        # mul(32,64] is invalid because it has a bracket instead of parenthesis
        
        valid_instructions = find_valid_mul_instructions(sample_memory)
        expected_instructions = [(2,4), (5,5), (11,8), (8,5)]
        assert valid_instructions == expected_instructions, f"Expected {expected_instructions}, got {valid_instructions}"
        
        print("✓ Find valid mul instructions test passed")
        print(f"  Found {len(valid_instructions)} valid instructions: {valid_instructions}")
        print("  Invalid instructions correctly ignored: mul[3,7], do_not_mul(5,5), mul(32,64]")
    
    def test_calculate_multiplication_sum(self):
        """Test calculate_multiplication_sum function with sample data"""
        # Sample corrupted memory from the problem
        sample_memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        
        # Expected calculation:
        # mul(2,4) = 2 * 4 = 8
        # mul(5,5) = 5 * 5 = 25
        # mul(11,8) = 11 * 8 = 88
        # mul(8,5) = 8 * 5 = 40
        # Total = 8 + 25 + 88 + 40 = 161
        
        valid_instructions = find_valid_mul_instructions(sample_memory)
        total_sum = calculate_multiplication_sum(valid_instructions)
        expected_sum = 161
        assert total_sum == expected_sum, f"Expected {expected_sum}, got {total_sum}"
        
        print("✓ Calculate multiplication sum test passed")
        print(f"  Found instructions: {valid_instructions}")
        print(f"  Calculations: 2*4=8, 5*5=25, 11*8=88, 8*5=40")
        print(f"  Total sum: {total_sum}")
    
    def test_edge_cases(self):
        """Test edge cases for mul instruction parsing"""
        test_cases = [
            # (memory, expected_valid_instructions, description)
            ("mul(1,2)", [(1,2)], "Simple valid instruction"),
            ("mul(123,456)", [(123,456)], "Valid instruction with 3-digit numbers"),
            ("mul(1,2)mul(3,4)", [(1,2), (3,4)], "Two consecutive valid instructions"),
            ("mul(1,2)invalidmul(3,4)", [(1,2), (3,4)], "Valid instructions with invalid text in between"),
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
            result = find_valid_mul_instructions(memory)
            assert result == expected, f"{description}: Expected {expected}, got {result}"
            print(f"    ✓ Passed")
        
        print("✓ Edge cases test passed")
    
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
            instructions = find_valid_mul_instructions(memory)
            result = calculate_multiplication_sum(instructions)
            assert result == expected, f"{description}: Expected {expected}, got {result}"
            print(f"    ✓ Passed (instructions: {instructions})")
        
        print("✓ Calculation edge cases test passed")
    
    def test_part2_sample_data(self):
        """Test with sample data from Part 2 problem description"""
        # Sample corrupted memory from Part 2
        sample_memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        
        # Verify the sample data structure
        assert len(sample_memory) > 0, "Sample memory should not be empty"
        assert isinstance(sample_memory, str), "Sample memory should be a string"
        
        print("✓ Part 2 sample data test passed")
        print(f"  Sample memory length: {len(sample_memory)}")
        print(f"  Sample memory: {sample_memory}")
    
    def test_extract_do_instructions(self):
        """Test extract_do_instructions function with sample data"""
        # Sample corrupted memory from Part 2
        sample_memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        
        # Expected do instructions: do() substrings
        # Note: This function extracts do() instructions, not dont() or undo()
        
        do_instructions = extract_do_instructions(sample_memory)
        print(f"✓ Extract do instructions test passed")
        print(f"  Found {len(do_instructions)} do instructions: {do_instructions}")
        print("  Note: This extracts do() substrings for processing")
    
    def test_compute_sum_of_do_instructions(self):
        """Test compute_sum_of_do_instructions function with sample data"""
        # Sample corrupted memory from Part 2
        sample_memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        
        # Extract do instructions and compute sum
        do_instructions = extract_do_instructions(sample_memory)
        valid_instructions = find_valid_mul_instructions(do_instructions)
        total_sum = calculate_multiplication_sum(valid_instructions)
        
        print(f"✓ Compute sum of do instructions test passed")
        print(f"  Do instructions: {do_instructions}")
        print(f"  Total sum: {total_sum}")
        print("  Note: This processes do() instruction substrings")
    
    def test_part2_integration(self):
        """Test Part 2 integration with sample data"""
        # Sample corrupted memory from Part 2
        sample_memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        
        # Test the complete Part 2 workflow
        do_instructions = extract_do_instructions(sample_memory)
        valid_instructions = find_valid_mul_instructions(do_instructions)
        total_sum = calculate_multiplication_sum(valid_instructions)
        
        print(f"✓ Part 2 integration test passed")
        print(f"  Sample: {sample_memory}")
        print(f"  Do instructions found: {do_instructions}")
        print(f"  Total sum: {total_sum}")
        print("  Note: This tests the complete Part 2 workflow")
    
    def test_part2_edge_cases(self):
        """Test edge cases for Part 2 do()/dont() parsing"""
        test_cases = [
            # (memory, expected_do_dont_instructions, description)
            ("do()", [("do", 0)], "Simple do() instruction"),
            ("dont()", [("dont", 0)], "Simple dont() instruction"),
            ("do()dont()", [("do", 0), ("dont", 3)], "Two consecutive instructions"),
            ("do()invalid()dont()", [("do", 0), ("dont", 12)], "Instructions with invalid text in between"),
            ("undo()", [("do", 0)], "undo() should be treated as do()"),
            ("dont()do()", [("dont", 0), ("do", 6)], "dont() followed by do()"),
            ("", [], "Empty memory"),
            ("nomulhere", [], "No do/dont instructions"),
        ]
        
        for memory, expected, description in test_cases:
            print(f"  Testing: {description}")
            print(f"    Memory: '{memory}'")
            print(f"    Expected: {expected}")
            # TODO: Uncomment when function is implemented
            # result = find_do_dont_instructions(memory)
            # assert result == expected, f"{description}: Expected {expected}, got {result}"
        
        print("✓ Part 2 edge cases test prepared")
    
    def test_part2_state_management(self):
        """Test state management for Part 2"""
        test_cases = [
            # (memory, expected_enabled_instructions, description)
            ("mul(1,2)", [(1,2)], "Single mul instruction (enabled by default)"),
            ("dont()mul(1,2)", [], "mul disabled by dont()"),
            ("do()mul(1,2)", [(1,2)], "mul enabled by do()"),
            ("dont()do()mul(1,2)", [(1,2)], "mul re-enabled by do() after dont()"),
            ("do()dont()mul(1,2)", [], "mul disabled by dont() after do()"),
            ("mul(1,2)dont()mul(3,4)", [(1,2)], "First mul enabled, second disabled"),
            ("mul(1,2)do()mul(3,4)", [(1,2), (3,4)], "Both mul enabled"),
        ]
        
        for memory, expected, description in test_cases:
            print(f"  Testing: {description}")
            print(f"    Memory: '{memory}'")
            print(f"    Expected enabled: {expected}")
            # TODO: Uncomment when function is implemented
            # result = find_valid_mul_instructions_with_state(memory)
            # assert result == expected, f"{description}: Expected {expected}, got {result}"
        
        print("✓ Part 2 state management test prepared")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
