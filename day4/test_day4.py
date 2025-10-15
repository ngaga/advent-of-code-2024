#!/usr/bin/env python3
"""
Advent of Code 2024 - Day 4 Tests
"""

import pytest

from day4.day4 import find_xmas_occurrences, count_xmas_in_grid, find_x_mas_patterns, count_x_mas_in_grid

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
            "XMASXMAS..",
            ".........",
            "........."
        ]
        
        occurrences = find_xmas_occurrences(grid)
        expected_count = 2  # Two XMAS occurrences
        
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
        # Grid with XMAS in all 8 directions from center (position 4,4)
        grid = [
            "X........",  # Diagonal up-left
            ".M.......",  # Vertical up
            "..A......",  # Diagonal up-right
            "...S.....",  # Horizontal left
            "XMASXMASX",  # Center row with XMAS left and right
            ".....S...",  # Horizontal right
            "......A..",  # Diagonal down-right
            ".......M.",  # Vertical down
            "........X"   # Diagonal down-left
        ]
        
        occurrences = find_xmas_occurrences(grid)
        expected_count = 4  # Four XMAS found in this grid
        
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
            "XMASXMASXMAS",  # Multiple overlapping XMAS
            "............",
            "............"
        ]
        
        occurrences = find_xmas_occurrences(grid)
        # Should find: XMAS (0,0-3), XMAS (0,4-7), XMAS (0,7-10)
        expected_count = 3
        
        assert len(occurrences) == expected_count, f"Expected {expected_count} occurrences, got {len(occurrences)}"
        
        print("✓ Complex overlapping test passed")
        print(f"  Found {len(occurrences)} XMAS in complex overlapping scenario")

class TestDay4Part2Solution:
    """Test cases for Day 4 Part 2 solution - X-MAS patterns"""
    
    def test_simple_x_mas_pattern(self):
        """Test finding simple X-MAS pattern"""
        grid = [
            "M.S",
            ".A.",
            "M.S"
        ]
        
        x_mas_occurrences = find_x_mas_patterns(grid)
        expected_count = 1
        
        assert len(x_mas_occurrences) == expected_count, f"Expected {expected_count} X-MAS patterns, got {len(x_mas_occurrences)}"
        print("✓ Simple X-MAS pattern test passed")
        print(f"  Found {len(x_mas_occurrences)} X-MAS patterns")
    
    def test_x_mas_with_backwards_mas(self):
        """Test X-MAS with backwards MAS"""
        grid = [
            "S.M",
            ".A.",
            "S.M"
        ]
        
        x_mas_occurrences = find_x_mas_patterns(grid)
        expected_count = 1
        
        assert len(x_mas_occurrences) == expected_count, f"Expected {expected_count} X-MAS patterns, got {len(x_mas_occurrences)}"
        print("✓ X-MAS with backwards MAS test passed")
        print(f"  Found {len(x_mas_occurrences)} X-MAS patterns")
    
    def test_multiple_x_mas_patterns(self):
        """Test multiple X-MAS patterns in grid"""
        grid = [
            "M.S.M.S",
            ".A...A.",
            "M.S.M.S"
        ]
        
        x_mas_occurrences = find_x_mas_patterns(grid)
        expected_count = 2
        
        assert len(x_mas_occurrences) == expected_count, f"Expected {expected_count} X-MAS patterns, got {len(x_mas_occurrences)}"
        print("✓ Multiple X-MAS patterns test passed")
        print(f"  Found {len(x_mas_occurrences)} X-MAS patterns")
    
    def test_problem_sample_grid_part2(self):
        """Test with the exact sample grid from Part 2 problem"""
        sample_grid = [
            ".M.S......",
            "..A..MSMS.",
            ".M.S.MAA..",
            "..A.ASMSM.",
            ".M.S.M....",
            "..........",
            "S.S.S.S.S.",
            ".A.A.A.A..",
            "M.M.M.M.M.",
            ".........."
        ]
        
        x_mas_occurrences = find_x_mas_patterns(sample_grid)
        expected_count = 9  # As stated in the problem
        
        assert len(x_mas_occurrences) == expected_count, f"Expected {expected_count} X-MAS patterns, got {len(x_mas_occurrences)}"
        
        print("✓ Problem sample grid Part 2 test passed")
        print(f"  Found {len(x_mas_occurrences)} X-MAS patterns in sample grid")
        print("  Expected: 9 patterns as stated in problem")
    
    def test_count_x_mas_in_grid(self):
        """Test count_x_mas_in_grid function with sample data"""
        sample_grid = [
            ".M.S......",
            "..A..MSMS.",
            ".M.S.MAA..",
            "..A.ASMSM.",
            ".M.S.M....",
            "..........",
            "S.S.S.S.S.",
            ".A.A.A.A..",
            "M.M.M.M.M.",
            ".........."
        ]
        
        total_count = count_x_mas_in_grid(sample_grid)
        expected_count = 9
        
        assert total_count == expected_count, f"Expected {expected_count} total X-MAS patterns, got {total_count}"
        
        print("✓ Count X-MAS in grid test passed")
        print(f"  Total X-MAS count: {total_count}")
    
    def test_x_mas_edge_cases(self):
        """Test edge cases for X-MAS pattern search"""
        test_cases = [
            # (grid, expected_count, description)
            ([
                "M.S",
                ".A.",
                "M.S"
            ], 1, "Single X-MAS pattern"),
            ([
                "M.S.M.S",
                ".A...A.",
                "M.S.M.S"
            ], 2, "Two X-MAS patterns in same grid"),
            ([
                "S.M",
                ".A.",
                "S.M"
            ], 1, "X-MAS with backwards MAS"),
            ([
                "M.A",
                ".S.",
                "M.A"
            ], 0, "Wrong pattern (not X-MAS)"),
            ([
                "...",
                "...",
                "..."
            ], 0, "Empty pattern"),
            ([
                "M",
                "A",
                "S"
            ], 0, "Too small for X-MAS pattern"),
            ([
                "M.S",
                ".A.",
                "M.S",
                "...",
                "M.S",
                ".A.",
                "M.S"
            ], 2, "Two X-MAS patterns in larger grid"),
        ]
        
        for grid, expected, description in test_cases:
            print(f"  Testing: {description}")
            print(f"    Grid: {grid}")
            print(f"    Expected count: {expected}")
            result = count_x_mas_in_grid(grid)
            assert result == expected, f"{description}: Expected {expected}, got {result}"
            print(f"    ✓ Passed")
        
        print("✓ X-MAS edge cases test passed")
    
    def test_x_mas_different_orientations(self):
        """Test X-MAS patterns in different orientations"""
        test_cases = [
            # (grid, expected_count, description)
            ([
                "M.S",
                ".A.",
                "M.S"
            ], 1, "Standard X-MAS orientation"),
            ([
                "S.M",
                ".A.",
                "S.M"
            ], 1, "X-MAS with backwards MAS"),
            ([
                "M.S",
                ".A.",
                "S.M"
            ], 0, "Mixed orientation (not valid X-MAS)"),
            ([
                "S.M",
                ".A.",
                "M.S"
            ], 0, "Mixed orientation (not valid X-MAS)"),
        ]
        
        for grid, expected, description in test_cases:
            print(f"  Testing: {description}")
            print(f"    Grid: {grid}")
            print(f"    Expected count: {expected}")
            result = count_x_mas_in_grid(grid)
            assert result == expected, f"{description}: Expected {expected}, got {result}"
            print(f"    ✓ Passed")
        
        print("✓ X-MAS different orientations test passed")
    
    def test_large_x_mas_grid(self):
        """Test with a larger grid containing multiple X-MAS patterns"""
        # Create a 10x10 grid with some X-MAS patterns scattered around
        grid = []
        for i in range(10):
            if i == 1:
                grid.append(".M.S......")
            elif i == 2:
                grid.append("..A.......")
            elif i == 3:
                grid.append(".M.S......")
            elif i == 6:
                grid.append("S.M.......")
            elif i == 7:
                grid.append(".A........")
            elif i == 8:
                grid.append("S.M.......")
            else:
                grid.append("." * 10)
        
        x_mas_occurrences = find_x_mas_patterns(grid)
        expected_count = 2  # Two X-MAS patterns in the grid
        
        assert len(x_mas_occurrences) == expected_count, f"Expected {expected_count} X-MAS patterns, got {len(x_mas_occurrences)}"
        
        print("✓ Large X-MAS grid test passed")
        print(f"  Found {len(x_mas_occurrences)} X-MAS patterns in 10x10 grid")
    
    def test_overlapping_x_mas_patterns(self):
        """Test overlapping X-MAS patterns"""
        grid = [
            "M.S.M.S",
            ".A...A.",
            "M.S.M.S"
        ]
        
        x_mas_occurrences = find_x_mas_patterns(grid)
        expected_count = 2  # Two overlapping X-MAS patterns
        
        assert len(x_mas_occurrences) == expected_count, f"Expected {expected_count} X-MAS patterns, got {len(x_mas_occurrences)}"
        
        print("✓ Overlapping X-MAS patterns test passed")
        print(f"  Found {len(x_mas_occurrences)} overlapping X-MAS patterns")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])