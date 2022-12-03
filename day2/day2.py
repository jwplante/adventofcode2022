from enum import Enum
import sys
from typing import Iterator

"""
Advent of Code Day 2 Solution
"""

__author__ = "James Plante (jwplante)"
__license__ = "MIT"

class GameChoice(Enum):
    ROCK = "ROCK",
    PAPER = "PAPER",
    SCISSORS = "SCISSORS"

def play_turn(your_move: GameChoice, opponent_move: GameChoice) -> int:
    """
    Plays a Turn of Rock Paper Scissors and returns the final score.
    :param your_move: Your Move
    :param opponent_move: Your opponent's move
    :return: Final score for the round
    """
    shape_value = {
        GameChoice.ROCK: 1,
        GameChoice.PAPER: 2,
        GameChoice.SCISSORS: 3
    }

    possible_outcomes = {
        GameChoice.ROCK: {
            GameChoice.ROCK: 3,
            GameChoice.PAPER: 0,
            GameChoice.SCISSORS: 6
        },
        GameChoice.PAPER: {
            GameChoice.ROCK: 6,
            GameChoice.PAPER: 3,
            GameChoice.SCISSORS: 0
        },
        GameChoice.SCISSORS: {
            GameChoice.ROCK: 0,
            GameChoice.PAPER: 6,
            GameChoice.SCISSORS: 3
        }
    }
    return shape_value[your_move] + possible_outcomes[your_move][opponent_move]


def part_one(contents: Iterator[str]):
    def char_to_move(move: str) -> GameChoice:
        """
        Gets the corresponding move based on the letter provided
        """
        if move == 'A' or move == 'X':
            return GameChoice.ROCK
        elif move == 'B' or move == 'Y':
            return GameChoice.PAPER
        elif move == 'C' or move == 'Z':
            return GameChoice.SCISSORS

    total_score = 0
    for turn in contents:
        moves = turn.strip().split()
        opponent_move = char_to_move(moves[0].strip())
        your_move = char_to_move(moves[1].strip())
        total_score += play_turn(your_move, opponent_move)
    
    print(f"Solution for Part 1: {total_score}")


def part_two(contents: Iterator[str]):
    def char_to_move(move: str) -> GameChoice:
        """
        Gets the corresponding move based on the letter provided
        - not based on assumption this time
        """
        if move == 'A':
            return GameChoice.ROCK
        elif move == 'B':
            return GameChoice.PAPER
        elif move == 'C':
            return GameChoice.SCISSORS
    
    move_to_lose = { # Given opponent move, how to win
        GameChoice.ROCK: GameChoice.SCISSORS,
        GameChoice.PAPER: GameChoice.ROCK,
        GameChoice.SCISSORS: GameChoice.PAPER
    }

    move_to_win = { # Given opponent move, how to lose
        GameChoice.ROCK: GameChoice.PAPER,
        GameChoice.PAPER: GameChoice.SCISSORS,
        GameChoice.SCISSORS: GameChoice.ROCK
    }

    total_score = 0
    for turn in contents:
        moves = turn.strip().split()
        opponent_move = char_to_move(moves[0].strip())
        your_intention = moves[1].strip()

        if your_intention == 'X': # Need to lose
            your_move = move_to_lose[opponent_move]
        elif your_intention == 'Y': # Need to draw
            your_move = opponent_move
        else: # Need to win
            your_move = move_to_win[opponent_move]
        
        total_score += play_turn(your_move, opponent_move)
    
    print(f"Solution for Part 2: {total_score}")



if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]

        with open(filename) as f:
            contents = f.readlines()

        part_one(contents) 
        part_two(contents)