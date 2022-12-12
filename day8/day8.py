import sys
import numpy as np

"""
Advent of Code Day 8 Solution
"""

__author__ = "James Plante (jwplante)"
__license__ = "MIT"

def str_to_mat(contents):
    matrix_lines = [line.strip() for line in contents.split('\n') if line != '']
    h = len(matrix_lines)
    w = len(matrix_lines[0])
    new_mat = np.zeros(dtype=np.int8, shape=(h, w))
    for i, line in enumerate(matrix_lines):
        for j, char in enumerate(line):
            new_mat[i][j] = int(char)
    return new_mat


def scenic_score(matrix, i, j) -> int:
    h, w = matrix.shape
    current_element = matrix[i][j]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    cursor_i = i
    cursor_j = j
    current_score = 1

    for dir_row, dir_col in directions:
        cursor_i = i
        cursor_j = j
        cursor_i += dir_row
        cursor_j += dir_col

        current_dir_score = 0
        while cursor_i >= 0 and cursor_j >= 0 and cursor_i < w and cursor_j < h:
            current_dir_score += 1
            if current_element <= matrix[cursor_i][cursor_j]:
                break
            cursor_i += dir_row
            cursor_j += dir_col

        current_score *= current_dir_score
    
    return current_score


def is_visible(matrix, i, j) -> bool:
    h, w = matrix.shape
    def on_the_edge():
        return i == 0 or j == 0 or i == h - 1 or j == w - 1
    
    def lower_trees_surrounding():
        current_element = matrix[i][j]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        cursor_i = i
        cursor_j = j
        is_visible = False

        for dir_row, dir_col in directions:
            cursor_i = i
            cursor_j = j
            cursor_i += dir_row
            cursor_j += dir_col

            encountered_tall_tree = False
            while cursor_i >= 0 and cursor_j >= 0 and cursor_i < w and cursor_j < h:
                if current_element <= matrix[cursor_i][cursor_j]:
                    encountered_tall_tree = True
                    break
                cursor_i += dir_row
                cursor_j += dir_col

            is_visible = is_visible or not encountered_tall_tree
        
        return is_visible
    
    return on_the_edge() or lower_trees_surrounding()


def part_one(contents):
    matrix = str_to_mat(contents)
    h, w = matrix.shape
    count = 0
    for i in range(h):
        for j in range(w):
            visible = is_visible(matrix, i, j)
            if visible:
                count += 1

    print(f"The Solution for Part 1: {count}")


def part_two(contents):
    matrix = str_to_mat(contents)
    h, w = matrix.shape
    max_score = 0
    for i in range(h):
        for j in range(w):
            max_score = max(max_score, scenic_score(matrix, i, j))

    print(f"The Solution for Part 2: {max_score}")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]

        with open(filename) as f:
            contents = f.read()

        part_one(contents) 
        part_two(contents)