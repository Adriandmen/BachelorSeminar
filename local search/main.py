from lib.LocalSearch import LocalSearch
from lib.board import Board


if __name__ == '__main__':
    # x = Board.from_board([
    #     [True, False, False, False],
    #     [False, False, False, True],
    #     [False, True, False, False],
    #     [False, True, False, False]
    # ])
    l = LocalSearch(8)
    s = l.search(n=10, retries=50)

    print("{} optimum with cost {} is:".format("Global" if s.cost() == 0 else "Local", s.cost()))
    print()
    print(s)
    print()
    # print(l.search_step(x))
