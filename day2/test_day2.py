#!/usr/bin/env python3
"""
Advent of Code 2024 - Day 2 Tests
"""

import pytest
import sys
import os

# Add the day2 directory to the path so we can import the module
sys.path.append(os.path.join(os.path.dirname(__file__)))

from solution import get_advent_of_code_data, count_safe_reports, is_safe_report

class TestDay2Solution:
    """Test cases for Day 2 solution"""
    
    def test_sample_data(self):
        """Test with sample data that was in data.txt"""
        # Sample data from the deleted data.txt file
        sample_data = [
            [7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [9, 7, 6, 2, 1],
            [1, 3, 2, 4, 5],
            [8, 6, 4, 4, 1],
            [1, 3, 6, 7, 9]
        ]
        
        # Verify the sample data structure
        assert len(sample_data) == 6, f"Expected 6 reports, got {len(sample_data)}"
        assert all(len(report) == 5 for report in sample_data), "All reports should have 5 values"
        
        print("✓ Sample data test passed")
        print(f"  Sample reports: {len(sample_data)}")
        print(f"  First report: {sample_data[0]}")
        print(f"  Last report: {sample_data[-1]}")
    
    def test_count_safe_reports(self):
        """Test count_safe_reports function with sample data"""
        # Sample data from the deleted data.txt file
        sample_data = [
            [7, 6, 4, 2, 1],  # Decreasing sequence with gaps of 1, 2, 2, 1 - should be safe
            [1, 2, 7, 8, 9],  # Mixed sequence with gap of 5 - should be unsafe
            [9, 7, 6, 2, 1],  # Mixed sequence with gap of 4 - should be unsafe
            [1, 3, 2, 4, 5],  # Mixed sequence - should be unsafe
            [8, 6, 4, 4, 1],  # Mixed sequence - should be unsafe
            [1, 3, 6, 7, 9]   # Increasing sequence with gaps of 2, 3, 1, 2 - should be safe
        ]
        
        # Test individual reports
        assert is_safe_report([7, 6, 4, 2, 1]), "Decreasing sequence should be safe"
        assert not is_safe_report([1, 2, 7, 8, 9]), "Sequence with gap > 3 should be unsafe"
        assert not is_safe_report([9, 7, 6, 2, 1]), "Mixed sequence should be unsafe"
        assert not is_safe_report([1, 3, 2, 4, 5]), "Mixed sequence should be unsafe"
        assert not is_safe_report([8, 6, 4, 4, 1]), "Mixed sequence should be unsafe"
        assert is_safe_report([1, 3, 6, 7, 9]), "Increasing sequence should be safe"
        
        # Test count_safe_reports function
        safe_count = count_safe_reports(sample_data)
        expected_safe = 2  # Only [7, 6, 4, 2, 1] and [1, 3, 6, 7, 9] are safe
        
        assert safe_count == expected_safe, f"Expected {expected_safe} safe reports, got {safe_count}"
        
        print("✓ Count safe reports test passed")
        print(f"  Total reports: {len(sample_data)}")
        print(f"  Safe reports: {safe_count}")
        print(f"  Unsafe reports: {len(sample_data) - safe_count}")
    
    def test_placeholder(self):
        """Placeholder test for Day 2"""
        # This test will always pass until Day 2 is implemented
        assert True, "Day 2 not implemented yet"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
