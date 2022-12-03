import sys
from typing import Iterator

"""
Advent of Code Day 1 Solution
"""

__author__ = "James Plante (jwplante)"
__license__ = "MIT"

def part_one(contents: Iterator[str]):
    max_cal_so_far = float('-inf')

    acc = 0
    for line in contents:
        # Check blank line
        if line.strip() == '':
            max_cal_so_far = max(max_cal_so_far, acc)
            acc = 0
        else:
            acc += int(line)

    print(f"Solution for part 1: {max_cal_so_far}")

def part_two(contents: Iterator[str]):
    elves = []

    acc = 0
    for line in contents:
        # Check blank line
        if line.strip() == '':
            elves.append(acc)
            acc = 0
        else:
            acc += int(line)

    elves.sort(reverse=True)
    top_three = elves[:3]
    print(f"Solution for part 2: {sum(top_three)}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]

        with open(filename) as f:
            contents = f.readlines()

        part_one(contents) 
        part_two(contents)

