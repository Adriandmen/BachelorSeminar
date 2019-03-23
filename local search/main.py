from lib.LocalSearch import LocalSearch
from lib.board import Board


if __name__ == '__main__':
    # x = Board.from_board([
    #     [True, False, False, False],
    #     [False, False, False, True],
    #     [False, True, False, False],
    #     [False, True, False, False]
    # ])
    l = LocalSearch(16)
    l.search(n=20, retries=20)
    # print(l.search_step(x))
