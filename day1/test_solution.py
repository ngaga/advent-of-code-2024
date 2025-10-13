import pytest
import sys
import os

# Add the day1 directory to the path so we can import the module
sys.path.append(os.path.join(os.path.dirname(__file__), 'day1'))

from solution import sortedDistance

class TestDay1Algorithm:
    """Test cases for the Day 1 sorted distance algorithm"""
    
    def test_basic_example(self):
        """Test with the original example values"""
        a = [3, 4, 2, 1, 3, 3]
        b = [4, 3, 5, 3, 9, 3]
        
        result = sortedDistance(a, b)
        expected = 11
        
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_simple_case(self):
        """Test with simple case"""
        a = [1, 2]
        b = [3, 4]
        
        result = sortedDistance(a, b)
        expected = 4  # |1-3| + |2-4| = 2 + 2 = 4
        
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_identical_lists(self):
        """Test with identical lists"""
        a = [1, 2, 3]
        b = [1, 2, 3]
        
        result = sortedDistance(a, b)
        expected = 0  # All distances should be 0
        
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_single_element(self):
        """Test with single element lists"""
        a = [5]
        b = [3]
        
        result = sortedDistance(a, b)
        expected = 2  # |5-3| = 2
        
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_empty_lists(self):
        """Test with empty lists"""
        a = []
        b = []
        
        result = sortedDistance(a, b)
        expected = 0  # Sum of empty list is 0
        
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_different_lengths(self):
        """Test with lists of different lengths"""
        a = [1, 2, 3]
        b = [4, 5]
        
        # This should work because zip stops at the shorter list
        result = sortedDistance(a, b)
        expected = 6  # |1-4| + |2-5| = 3 + 3 = 6
        
        assert result == expected, f"Expected {expected}, got {result}"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
