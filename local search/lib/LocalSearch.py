from lib.board import Board

l = False


def log(string=None):
    if l:
        if string is None:
            print()
        else:
            print(string)


class LocalSearch:

    def __init__(self, size: int):
        self.size = size
        self.optimum = Board(size)
        self.optimal_cost = self.optimum.cost()

    def search_step(self, optimum: Board):
        """
        Step searches the new optimal neighbour in a greedy manner. The optimal neighbour is returned
        if there exists an improvement. Otherwise, None is returned.
        :param optimum: The board from which the neighbourhood will be checked.
        :return: The improved Board or None if there does not exist any.
        """

        optimal_cost = optimum.cost()

        curr_optimum = optimum
        curr_cost = optimal_cost
        for neighbour in curr_optimum.neighbourhood():
            if curr_optimum is None or curr_cost > neighbour.cost():
                curr_optimum = neighbour
                curr_cost = neighbour.cost()

        if curr_cost < optimal_cost:
            return curr_optimum
        else:
            return None

    def search(self, n=10, retries=20):
        """
        Attempts to find the optimal solution to the n-Queens problem using local search
        where the maximum number of retries is given. Each retry has a maximum of 'n'
        search steps.
        :param n: The maximum number of search steps for each retry.
        :param retries: The number of retries.
        :return: The optimum found by the local search algorithm.
        """

        for retry in range(retries):
            curr_optimum = Board(self.size)

            for step in range(n):
                x = self.search_step(curr_optimum)
                if x is None:
                    break

                curr_optimum = x
            if curr_optimum.cost() < self.optimal_cost:
                self.optimum = curr_optimum
                self.optimal_cost = curr_optimum.cost()

            if self.optimal_cost == 0:
                return self.optimum
        return self.optimum
