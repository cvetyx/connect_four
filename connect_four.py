from dataclasses import dataclass
from typing import List
from my_classes import *


def get_data():
    with open('test.txt') as f:
        players = f.readline().strip().split(',')
        moves = [Move(int(move[1]) - 1, move[0]) for move in f.readline().strip().split(",")]
        # print(moves)
        return players, moves


def main():
    board = Board()
    players, moves = get_data()

    def flip_board():
        new_board = [el for el in zip(*board.board)]
        result = [list(t) for t in new_board[::-1]]
        for line in result:
            print(line)

    def play_game():
        for i, move in enumerate(moves):
            print(f"Move number {i + 1}: {move}")
            board.play_move(move)
            if check_winner(move):
                print(f"Player {players[i % 2]} won on move {i + 1} with {move}")

        flip_board()

    def check_winner(move: Move):
        # checking horizontal
        current_index = move.index
        for row in range(6):
            for col in range(4):
                if board.board[row][col] == current_index and \
                        board.board[row][col + 1] == current_index and \
                        board.board[row][col + 2] == current_index and \
                        board.board[row][col + 3] == current_index:
                    return True

        # # checking vertical
        # for row in range(3):
        #     for col in range(7):
        #         if board.board[row][col] == player1_data and \
        #                 board.board[row + 1][col] == player1_data and \
        #                 board.board[row + 2][col] == player1_data and \
        #                 board.board[row + 3][col] == player1_data:
        #             return True
        #
        # # checking diagonal
        # for row in range(3):
        #     for col in range(4):
        #         if board.board[row][col] == player and \
        #                 board.board[row + 1][col + 1] == player and \
        #                 board.board[row + 2][col + 2] == player and \
        #                 board.board[row + 3][col + 3] == player:
        #             return True
        #         if board.board[row][col + 3] == player and \
        #                 board.board[row + 1][col + 2] == player and \
        #                 board.board[row + 2][col + 1] == player and \
        #                 board.board[row + 3][col] == player:
        #             return True
        return False

    play_game()


main()
