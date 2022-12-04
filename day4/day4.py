import sys
from typing import Sequence, Tuple

"""
Advent of Code 2022 Day 4 Solution
"""

__author__ = "James Plante (jwplante)"
__license__ = "MIT"

def parse_line_into_range(line: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Parses one line of input into two range tuples
    """
    split = line.strip().split(',')
    range_1 = tuple([int(i) for i in split[0].split('-')])
    range_2 = tuple([int(i) for i in split[1].split('-')])
    return range_1, range_2

def part_one(lines: Sequence[str]):
    def is_fully_contained(one: Tuple[int, int], other: Tuple[int, int]) -> bool:
        """
        Checks if one range is fully contained within the other
        :param one: Range 1 (assuming a sorted tuple)
        :param other: Range 2 (assuming a sorted tuple)
        :return: true if yes, false if no
        """
        def construct_inner_pair(one: Tuple[int, int], other: Tuple[int, int]) -> Tuple[int, int]:
            lower = one[0] if one[0] >= other[0] else other[0]
            higher = one[1] if one[1] <= other[1] else other[1]
            return tuple(sorted((lower, higher)))

        lower, higher = construct_inner_pair(one, other)
        return (lower, higher) == one or (lower, higher) == other
    contained_pairs = 0
    for line in lines:
        range_one, range_two = parse_line_into_range(line)
        if is_fully_contained(range_one, range_two):
            contained_pairs += 1
    
    print(f"Solution to Part 1: {contained_pairs}")


def part_two(lines: Sequence[str]):

    def is_contained(one: Tuple[int, int], other: Tuple[int, int]) -> bool:
        """
        Check if there is any overlap between the two ranges
        :param one: One range
        :param two: The other range
        :return: 
        """
        lower_range = one if one[0] < other[0] else other
        higher_range = other if one[0] < other[0] else one
        
        return lower_range[1] >= higher_range[0]

    contained_pairs = 0
    for line in lines:
        range_one, range_two = parse_line_into_range(line)
        if is_contained(range_one, range_two):
            contained_pairs += 1
    
    print(f"Solution to Part 2: {contained_pairs}")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]

        with open(filename) as f:
            contents = f.readlines()

        part_one(contents) 
        part_two(contents)