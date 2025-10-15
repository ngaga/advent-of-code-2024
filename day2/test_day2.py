#!/usr/bin/env python3
"""
Advent of Code 2024 - Day 2 Tests
"""

import pytest

from day2.day2 import count_safe_reports, is_safe_report, is_safe_by_one_report, count_safe_reports_by_one_report

class TestDay2Solution:
    """Test cases for Day 2 solution"""
    
    def test_sample_data(self):
        """Test with sample data that was in data.txt"""
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
    
    def test_problem_dampener_individual_reports(self):
        """Test individual reports with Problem Dampener (Part Two)"""
        # Test cases from the problem description
        test_cases = [
            # (report, expected_safe_with_dampener, description)
            ([7, 6, 4, 2, 1], True, "Safe without removing any level"),
            ([1, 2, 7, 8, 9], False, "Unsafe regardless of which level is removed"),
            ([9, 7, 6, 2, 1], False, "Unsafe regardless of which level is removed"),
            ([1, 3, 2, 4, 5], True, "Safe by removing the second level, 3"),
            ([8, 6, 4, 4, 1], True, "Safe by removing the third level, 4"),
            ([1, 3, 6, 7, 9], True, "Safe without removing any level")
        ]
        
        for report, expected, description in test_cases:
            result = is_safe_by_one_report(report)
            assert result == expected, f"Report {report}: {description}. Expected {expected}, got {result}"
            print(f"✓ {description}: {report} -> {result}")
    
    def test_problem_dampener_count(self):
        """Test count_safe_reports_by_one_report with sample data"""
        # Sample data from the problem description
        sample_data = [
            [7, 6, 4, 2, 1],  # Safe without removing any level
            [1, 2, 7, 8, 9],  # Unsafe regardless of which level is removed
            [9, 7, 6, 2, 1],  # Unsafe regardless of which level is removed
            [1, 3, 2, 4, 5],  # Safe by removing the second level, 3
            [8, 6, 4, 4, 1],  # Safe by removing the third level, 4
            [1, 3, 6, 7, 9]   # Safe without removing any level
        ]
        
        # Test count_safe_reports_by_one_report function
        safe_count = count_safe_reports_by_one_report(sample_data)
        expected_safe = 4  # 4 reports are actually safe with Problem Dampener
        
        assert safe_count == expected_safe, f"Expected {expected_safe} safe reports with Problem Dampener, got {safe_count}"
        
        print("✓ Problem Dampener count test passed")
        print(f"  Total reports: {len(sample_data)}")
        print(f"  Safe reports with Problem Dampener: {safe_count}")
        print(f"  Unsafe reports even with Problem Dampener: {len(sample_data) - safe_count}")
    
    def test_problem_dampener_edge_cases(self):
        """Test edge cases for Problem Dampener"""
        # Test with very short reports
        assert is_safe_by_one_report([1]), "Single value should be safe"
        assert is_safe_by_one_report([1, 2]), "Two values should be safe"
        assert is_safe_by_one_report([2, 1]), "Two values should be safe"
        
        # Test with reports that need exactly one removal
        assert is_safe_by_one_report([1, 5, 2, 3]), "Should be safe by removing 5"
        assert is_safe_by_one_report([1, 2, 5, 3, 4]), "Should be safe by removing 5"
        
        # Test with reports that are still unsafe even with one removal
        assert not is_safe_by_one_report([1, 5, 2, 6]), "Should be unsafe even with one removal"
        assert not is_safe_by_one_report([1, 2, 3, 1, 2, 3]), "Should be unsafe even with one removal"
        
        print("✓ Problem Dampener edge cases test passed")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
