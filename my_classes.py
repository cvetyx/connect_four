from typing import List
from dataclasses import dataclass


@dataclass(init=True)
class Move:
    index: int
    color: str


class PlayerData:
    def __init__(self, name: str, moves: List[Move]):
        self.name = name
        self.moves = moves
        self.counter = 0

    def __iter__(self):
        return PlayerData(self.name, self.moves)

    def __next__(self):
        if self.counter >= len(self.moves):
            raise StopIteration()

        element = self.moves[self.counter]
        self.counter += 1
        return element


class Board:
    def __init__(self):
        self.board = [[] for _ in range(7)]

    def play_move(self, move: Move):
        self.board[move.index].append(move.color)

