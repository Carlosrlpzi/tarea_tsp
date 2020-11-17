"""
"""


class Solver:
    """"""

    def __init__(self, algorithms):
        self.algorithms = algorithms
        self.solutions = {}

    def solve(self, tsp):
        print(f"Usaremos {len(self.algorithms)} algoritmos para resolver este problema.")
        for algorithm in self.algorithms:
            print(f"Solving TSP problem with {algorithm}")
            self.solutions[str(algorithm)] = algorithm.run(tsp)

        return self.solutions
