import re
import sys
from typing import List, Tuple

"""
Advent of Code 2022 Day 5 Solution
"""

__author__ = "James Plante (jwplante)"
__license__ = "MIT"

class Stack:
    def __init__(self, id: int):
        self.id = id
        self._stack = []

    def __len__(self):
        # Get length of stack
        return len(self.stacks)

    def push(self, item: str):
        # Push item onto stack
        self._stack.append(item)

    def pop(self) -> str:
        # Pop item off of stack
        return self._stack.pop()
    
    def peek(self):
        # Look at top item of stack
        return self._stack[-1]


class Dock:
    def __init__(self, size):
        self.size = size
        self.stacks: List[Stack] = [Stack(i + 1) for i in range(size)]
    
    def move(self, num_items: int, from_position: int, to_position: int, reverse=False):
        """
        Moves a set number of items from one position to another

        :param num_items: Number to items to move
        :param from_position: id of stack to take from
        :param to_position: id of stack to push items onto
        :param reverse: Whether or not it is in "9001 mode"
        """
        items_to_move = []

        for _ in range(num_items):
            items_to_move.append(self.stacks[from_position - 1].pop())
        
        if not reverse:
            items_to_move = items_to_move[::-1]
        
        for _ in range(num_items):
            item = items_to_move.pop()
            self.stacks[to_position - 1].push(item)


def parse(input_str: str) -> Tuple[Dock, List[Tuple[int, int]]]:
    """
    Parses the input string and returns a new Dock and list of move instructions
    """ 
    def parse_dock(dock_str: str) -> Dock:
        lines = dock_str.split('\n')
        header = lines[-1]
        # From the header make the dock object
        num_stacks = len(re.split(r'\s+', header.strip()))
        dock = Dock(num_stacks)
        
        # Parse the rest of the input and insert into stacks
        stack_lines = lines[-2::-1] 
        for stack in stack_lines:
            for result in re.finditer("\w+", stack):
                # Depending on char position, put in the correct stack
                stack_to_put = result.start() // 4
                dock.stacks[stack_to_put].push(result.group())

        return dock
    
    def parse_instructions(instruction_str: str) -> List[Tuple[int, int]]:
        instruction_lines = instruction_str.split('\n')
        line_pattern = re.compile(r"move (\d+) from (\d+) to (\d+)")
        instructions = []

        for line in instruction_lines:
            matches = re.findall(line_pattern, line)
            instruction = tuple([int(i) for i in matches[0]])
            instructions.append(instruction)
        
        return instructions

    dock_str, instructions_str = input_str.split("\n\n")
    dock = parse_dock(dock_str)
    instructions = parse_instructions(instructions_str)
    return dock, instructions

def part_one(input_str: str):
    dock, instructions = parse(input_str)
    for instruction in instructions:
        dock.move(*instruction)
    
    answer = ''.join([stack.peek() for stack in dock.stacks])
    
    print(f"The answer to Part 1 is {answer}") 


def part_two(input_str: str):
    dock, instructions = parse(input_str)
    for instruction in instructions:
        dock.move(*instruction, reverse=True)
    
    answer = ''.join([stack.peek() for stack in dock.stacks])
    
    print(f"The answer to Part 2 is {answer}") 


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]

        with open(filename) as f:
            contents = f.read()

        part_one(contents) 
        part_two(contents)