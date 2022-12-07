import sys

"""
Advent of Code 2022 Day 6 Solution
"""

__author__ = "James Plante (jwplante)"
__license__ = "MIT"

def all_different_chars(s: str) -> bool:
    unique_letters = set(s)
    return len(s) != 0 and len(s) == len(unique_letters)

def part_one(input_str: str):
    seek = -1
    for current in range(4, len(input_str)):
        window = input_str[(current - 4):current]
        if all_different_chars(window):
            seek = current
            break
    
    print(f"The answer to Part 1 is: {seek}")


def part_two(input_str: str):
    seek = -1
    for current in range(14, len(input_str)):
        window = input_str[(current - 14):current]
        if all_different_chars(window):
            seek = current
            break
    
    print(f"The answer to Part 2 is: {seek}")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]

        with open(filename) as f:
            contents = f.read()

        part_one(contents) 
        part_two(contents)