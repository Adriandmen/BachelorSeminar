from lib.LocalSearch import LocalSearch
from lib.board import Board

Q = True
_ = False

if __name__ == '__main__':
    x = Board.from_board([
        [Q, _, _, _],
        [_, Q, _, _],
        [Q, _, _, _],
        [_, Q, _, _]
    ]) # type: Board

    for neighbour in x.neighbourhood():
        print(neighbour)
        print()

    print("{} neighbours found.".format(len(x.neighbourhood())))

    # l = LocalSearch(8)
    # s = l.search(n=10, retries=50)
    #
    # print("{} optimum with cost {} is:".format("Global" if s.cost() == 0 else "Local", s.cost()))
    # print()
    # print(s)
    # print()
    # print(l.search_step(x))
