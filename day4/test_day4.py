#!/usr/bin/env python3
"""
Advent of Code 2024 - Day 4 Tests
"""

import pytest
import sys
import os

# Add the day4 directory to the path so we can import the module
sys.path.append(os.path.join(os.path.dirname(__file__)))

from solution import get_advent_of_code_data, find_xmas_occurrences, count_xmas_in_grid

class TestDay4Solution:
    """Test cases for Day 4 solution"""
    
    def test_sample_data(self):
        """Test with sample data from the problem description"""
        # Sample word search from the problem
        sample_grid = [
            "MMMSXXMASM",
            "MSAMXMSMSA", 
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX"
        ]
        
        # Verify the sample data structure
        assert len(sample_grid) == 10, f"Expected 10 rows, got {len(sample_grid)}"
        assert all(len(row) == 10 for row in sample_grid), "All rows should have 10 characters"
        
        print("✓ Sample data test passed")
        print(f"  Grid size: {len(sample_grid)}x{len(sample_grid[0])}")
        print(f"  First row: {sample_grid[0]}")
        print(f"  Last row: {sample_grid[-1]}")
    
    def test_simple_horizontal_xmas(self):
        """Test finding XMAS horizontally"""
        grid = [
            "XMAS.....",
            ".........",
            "........."
        ]
        
        occurrences = find_xmas_occurrences(grid)
        expected_count = 1
        
        assert len(occurrences) == expected_count, f"Expected {expected_count} occurrences, got {len(occurrences)}"
        print("✓ Simple horizontal XMAS test passed")
        print(f"  Found {len(occurrences)} horizontal XMAS")
    
    def test_simple_vertical_xmas(self):
        """Test finding XMAS vertically"""
        grid = [
            "X........",
            "M........",
            "A........",
            "S........",
            ".........",
            "........."
        ]
        
        occurrences = find_xmas_occurrences(grid)
        expected_count = 1
        
        assert len(occurrences) == expected_count, f"Expected {expected_count} occurrences, got {len(occurrences)}"
        print("✓ Simple vertical XMAS test passed")
        print(f"  Found {len(occurrences)} vertical XMAS")
    
    def test_simple_diagonal_xmas(self):
        """Test finding XMAS diagonally"""
        grid = [
            "X........",
            ".M.......",
            "..A......",
            "...S.....",
            ".........",
            "........."
        ]
        
        occurrences = find_xmas_occurrences(grid)
        expected_count = 1
        
        assert len(occurrences) == expected_count, f"Expected {expected_count} occurrences, got {len(occurrences)}"
        print("✓ Simple diagonal XMAS test passed")
        print(f"  Found {len(occurrences)} diagonal XMAS")
    
    def test_backwards_xmas(self):
        """Test finding XMAS written backwards"""
        grid = [
            "SAMX.....",
            ".........",
            "........."
        ]
        
        occurrences = find_xmas_occurrences(grid)
        expected_count = 1
        
        assert len(occurrences) == expected_count, f"Expected {expected_count} occurrences, got {len(occurrences)}"
        print("✓ Backwards XMAS test passed")
        print(f"  Found {len(occurrences)} backwards XMAS")
    
    def test_multiple_occurrences(self):
        """Test finding multiple XMAS occurrences"""
        grid = [
            "XMASXMAS.",
            ".........",
            "........."
        ]
        
        occurrences = find_xmas_occurrences(grid)
        expected_count = 2
        
        assert len(occurrences) == expected_count, f"Expected {expected_count} occurrences, got {len(occurrences)}"
        print("✓ Multiple occurrences test passed")
        print(f"  Found {len(occurrences)} XMAS occurrences")
    
    def test_overlapping_occurrences(self):
        """Test finding overlapping XMAS occurrences"""
        grid = [
            "XMASMAS..",
            ".........",
            "........."
        ]
        
        occurrences = find_xmas_occurrences(grid)
        expected_count = 2  # XMAS and SAMX (overlapping)
        
        assert len(occurrences) == expected_count, f"Expected {expected_count} occurrences, got {len(occurrences)}"
        print("✓ Overlapping occurrences test passed")
        print(f"  Found {len(occurrences)} overlapping XMAS occurrences")
    
    def test_problem_sample_grid(self):
        """Test with the exact sample grid from the problem"""
        sample_grid = [
            "MMMSXXMASM",
            "MSAMXMSMSA", 
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX"
        ]
        
        occurrences = find_xmas_occurrences(sample_grid)
        expected_count = 18  # As stated in the problem
        
        assert len(occurrences) == expected_count, f"Expected {expected_count} occurrences, got {len(occurrences)}"
        
        print("✓ Problem sample grid test passed")
        print(f"  Found {len(occurrences)} XMAS occurrences in sample grid")
        print("  Expected: 18 occurrences as stated in problem")
    
    def test_count_xmas_in_grid(self):
        """Test count_xmas_in_grid function with sample data"""
        sample_grid = [
            "MMMSXXMASM",
            "MSAMXMSMSA", 
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX"
        ]
        
        total_count = count_xmas_in_grid(sample_grid)
        expected_count = 18
        
        assert total_count == expected_count, f"Expected {expected_count} total XMAS, got {total_count}"
        
        print("✓ Count XMAS in grid test passed")
        print(f"  Total XMAS count: {total_count}")
    
    def test_edge_cases(self):
        """Test edge cases for XMAS search"""
        test_cases = [
            # (grid, expected_count, description)
            (["XMAS"], 1, "Single row with XMAS"),
            (["X", "M", "A", "S"], 1, "Single column with XMAS"),
            (["XMASXMAS"], 2, "Two XMAS in single row"),
            (["X", "M", "A", "S", "X", "M", "A", "S"], 2, "Two XMAS in single column"),
            (["...."], 0, "No XMAS in grid"),
            (["X"], 0, "Single character (not XMAS)"),
            (["XM"], 0, "Two characters (not XMAS)"),
            (["XMA"], 0, "Three characters (not XMAS)"),
            ([""], 0, "Empty row"),
            ([], 0, "Empty grid"),
        ]
        
        for grid, expected, description in test_cases:
            print(f"  Testing: {description}")
            print(f"    Grid: {grid}")
            print(f"    Expected count: {expected}")
            result = count_xmas_in_grid(grid)
            assert result == expected, f"{description}: Expected {expected}, got {result}"
            print(f"    ✓ Passed")
        
        print("✓ Edge cases test passed")
    
    def test_all_directions(self):
        """Test XMAS in all possible directions"""
        # Grid with XMAS in all 8 directions from center
        grid = [
            "S...X...A",  # Diagonal up-left to down-right
            "M...X...M",  # Vertical up and down
            "A...X...S",  # Diagonal up-right to down-left  
            "X...X...X",  # Horizontal left and right
            "A...X...S",  # Diagonal down-right to up-left
            "M...X...M",  # Vertical down and up
            "S...X...A",  # Diagonal down-left to up-right
            "X...X...X",  # Horizontal right and left
            "........."   # Empty row
        ]
        
        occurrences = find_xmas_occurrences(grid)
        expected_count = 8  # One in each direction
        
        assert len(occurrences) == expected_count, f"Expected {expected_count} occurrences, got {len(occurrences)}"
        
        print("✓ All directions test passed")
        print(f"  Found {len(occurrences)} XMAS in all directions")
    
    def test_large_grid(self):
        """Test with a larger grid"""
        # Create a 20x20 grid with some XMAS scattered around
        grid = []
        for i in range(20):
            if i == 0:
                grid.append("XMAS" + "." * 16)
            elif i == 10:
                grid.append("." * 10 + "XMAS" + "." * 6)
            elif i == 19:
                grid.append("." * 16 + "XMAS")
            else:
                grid.append("." * 20)
        
        occurrences = find_xmas_occurrences(grid)
        expected_count = 3  # Three XMAS in the grid
        
        assert len(occurrences) == expected_count, f"Expected {expected_count} occurrences, got {len(occurrences)}"
        
        print("✓ Large grid test passed")
        print(f"  Found {len(occurrences)} XMAS in 20x20 grid")
    
    def test_complex_overlapping(self):
        """Test complex overlapping scenarios"""
        # Grid with complex overlapping patterns
        grid = [
            "XMASMASXMAS",  # Multiple overlapping XMAS
            "...........",
            "..........."
        ]
        
        occurrences = find_xmas_occurrences(grid)
        # Should find: XMAS (0,0-3), SAMX (0,3-6), XMAS (0,7-10)
        expected_count = 3
        
        assert len(occurrences) == expected_count, f"Expected {expected_count} occurrences, got {len(occurrences)}"
        
        print("✓ Complex overlapping test passed")
        print(f"  Found {len(occurrences)} XMAS in complex overlapping scenario")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])