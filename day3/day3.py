import sys
from typing import Sequence

"""
Advent of Code Day 3 Solution
"""

__author__ = "James Plante (jwplante)"
__license__ = "MIT"

def get_priority(item_type: str) -> int:
    """
    Computes the priority value given a single char
    :param item_type: string containing one char with an alphanumeric character
    :return: the priority value
    """
    is_upper = item_type.isupper()
    ascii_offset = 0x41 if is_upper else 0x61
    priority_offset = 27 if is_upper else 1
    return ord(item_type) - ascii_offset + priority_offset

def part_one(lines: Sequence[str]):
    final_answer = 0
    for rucksack in lines:
        rucksack = rucksack.strip()

        pivot = len(rucksack) // 2
        left_compartment = rucksack[:pivot]
        right_compartment = rucksack[pivot:]
        left_item_types = set(left_compartment)
        right_item_types = set(right_compartment)

        common_types = left_item_types.intersection(right_item_types)
        final_answer += sum([get_priority(common_type) for common_type in common_types])
    print(f"Solution for Part 1: {final_answer}")


def part_two(lines: Sequence[str]):
    final_answer = 0
    lines = [line.strip() for line in lines]
    for group in range(0, len(lines), 3):
        rucksacks_for_group = [set(lines[group]), set(lines[group + 1]), set(lines[group + 2])]
        common_types = rucksacks_for_group[0] \
                        .intersection(rucksacks_for_group[1] \
                        .intersection(rucksacks_for_group[2]))
        final_answer += sum([get_priority(common_type) for common_type in common_types])

    print(f"Solution for Part 2: {final_answer}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]

        with open(filename) as f:
            contents = f.readlines()

        part_one(contents) 
        part_two(contents)