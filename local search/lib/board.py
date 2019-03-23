from typing import List
import random


class Board:

    def __init__(self, size: int):
        self.size = size
        self.board = [self.random_row() for _ in range(size)]

    @staticmethod
    def from_board(board: List[List[bool]]):
        """
        Creates a new Board instance from a List[List[Bool]] where 'True' represents
        a queen and 'False' represents an empty square on the chess board.
        :param board: The chess board, represented as a 2-dimensional list of booleans.
        :return: The corresponding Board instance.
        """
        new_board = Board(len(board))
        new_board.board = board

        return new_board

    def random_row(self):
        """
        Generates a random row with one queen, represented as 'True'.
        :return: The random row
        """
        row = ((self.size - 1) * [False]) + [True]
        random.shuffle(row)
        return row

    def cost(self):
        """
        Computes the number of pairs of threatening queens, also known as the cost
        of the current board.
        :return: The cost of the current position.
        """
        threat_count = 0

        for x1 in range(0, self.size - 1):
            for x2 in range(x1 + 1, self.size):
                y1 = self.board[x1].index(True)
                y2 = self.board[x2].index(True)

                if y1 == y2 or x1 - y1 == x2 - y2 or x1 + y1 == x2 + y2:
                    threat_count += 1

        return threat_count

    def neighbourhood(self) -> List['Board']:
        """
        Computes the neighbourhood of the current board by modifying a single row
        of the current Board.
        :return: All modified versions of the current Board.
        """
        neighbours = []

        for row_index in range(0, self.size):
            queen_index = self.board[row_index].index(True)

            for col_index in range(0, self.size):
                if col_index == queen_index:
                    continue

                new_row = [False] * self.size
                new_row[col_index] = True
                new_board = self.board[:]
                new_board[row_index] = new_row
                neighbours.append(Board.from_board(new_board))

        return neighbours

    def __repr__(self):
        return "\n".join(" ".join(["Q" if file else "." for file in row]) for row in self.board)

