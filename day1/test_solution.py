import pytest
import sys
import os

# Add the day1 directory to the path so we can import the module
sys.path.append(os.path.join(os.path.dirname(__file__), 'day1'))

from solution import sortedDistance, sort_lists, calculate_similarity_index

class TestDay1Algorithm:
    """Test cases for the Day 1 sorted distance algorithm"""
    
    def test_basic_example(self):
        """Test with the original example values"""
        a = [3, 4, 2, 1, 3, 3]
        b = [4, 3, 5, 3, 9, 3]
        
        # Sort the lists first
        sorted_a, sorted_b = sort_lists(a, b)
        
        result = sortedDistance(sorted_a, sorted_b)
        expected = 11
        
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_simple_case(self):
        """Test with simple case"""
        a = [1, 2]
        b = [3, 4]
        
        # Sort the lists first
        sorted_a, sorted_b = sort_lists(a, b)
        
        result = sortedDistance(sorted_a, sorted_b)
        expected = 4  # |1-3| + |2-4| = 2 + 2 = 4
        
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_identical_lists(self):
        """Test with identical lists"""
        a = [1, 2, 3]
        b = [1, 2, 3]
        
        # Sort the lists first
        sorted_a, sorted_b = sort_lists(a, b)
        
        result = sortedDistance(sorted_a, sorted_b)
        expected = 0  # All distances should be 0
        
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_single_element(self):
        """Test with single element lists"""
        a = [5]
        b = [3]
        
        # Sort the lists first
        sorted_a, sorted_b = sort_lists(a, b)
        
        result = sortedDistance(sorted_a, sorted_b)
        expected = 2  # |5-3| = 2
        
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_empty_lists(self):
        """Test with empty lists"""
        a = []
        b = []
        
        # Sort the lists first
        sorted_a, sorted_b = sort_lists(a, b)
        
        result = sortedDistance(sorted_a, sorted_b)
        expected = 0  # Sum of empty list is 0
        
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_different_lengths(self):
        """Test with lists of different lengths"""
        a = [1, 2, 3]
        b = [4, 5]
        
        # Sort the lists first
        sorted_a, sorted_b = sort_lists(a, b)
        
        # This should work because zip stops at the shorter list
        result = sortedDistance(sorted_a, sorted_b)
        expected = 6  # |1-4| + |2-5| = 3 + 3 = 6
        
        assert result == expected, f"Expected {expected}, got {result}"

class TestSimilarityIndex:
    """Test cases for the similarity index algorithm"""
    
    def test_basic_similarity(self):
        """Test with basic similarity case"""
        a = [1, 2, 3]
        b = [2, 3, 4]
        
        # Sort the lists first
        sorted_a, sorted_b = sort_lists(a, b)
        
        result = calculate_similarity_index(sorted_a, sorted_b)
        expected = 5  # 2 + 3 = 5 (common values)
        
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_no_common_values(self):
        """Test with no common values"""
        a = [1, 2, 3]
        b = [4, 5, 6]
        
        # Sort the lists first
        sorted_a, sorted_b = sort_lists(a, b)
        
        result = calculate_similarity_index(sorted_a, sorted_b)
        expected = 0  # No common values
        
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_identical_lists(self):
        """Test with identical lists"""
        a = [1, 2, 3]
        b = [1, 2, 3]
        
        # Sort the lists first
        sorted_a, sorted_b = sort_lists(a, b)
        
        result = calculate_similarity_index(sorted_a, sorted_b)
        expected = 6  # 1 + 2 + 3 = 6 (all values are common)
        
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_duplicate_values(self):
        """Test with duplicate values"""
        a = [1, 1, 2, 2]
        b = [1, 2, 2, 3]
        
        # Sort the lists first
        sorted_a, sorted_b = sort_lists(a, b)
        
        result = calculate_similarity_index(sorted_a, sorted_b)
        expected = 10  # 1*1 + 1*1 + 2*2 + 2*2 = 1 + 1 + 4 + 4 = 10
        
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_empty_lists(self):
        """Test with empty lists"""
        a = []
        b = []
        
        # Sort the lists first
        sorted_a, sorted_b = sort_lists(a, b)
        
        result = calculate_similarity_index(sorted_a, sorted_b)
        expected = 0  # No common values in empty lists
        
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_different_lengths(self):
        """Test with lists of different lengths"""
        a = [1, 2, 3, 4]
        b = [2, 3]
        
        # Sort the lists first
        sorted_a, sorted_b = sort_lists(a, b)
        
        result = calculate_similarity_index(sorted_a, sorted_b)
        expected = 5  # 2 + 3 = 5 (common values)
        
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_specific_example(self):
        """Test with the specific example from the problem"""
        a = [3, 4, 2, 1, 3, 3]
        b = [4, 3, 5, 3, 9, 3]
        
        # Sort the lists first
        sorted_a, sorted_b = sort_lists(a, b)
        
        result = calculate_similarity_index(sorted_a, sorted_b)
        expected = 31  # 9 + 4 + 0 + 0 + 9 + 9 = 31
        
        assert result == expected, f"Expected {expected}, got {result}"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
