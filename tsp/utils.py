import importlib
from itertools import product


def process_grid(grids):
    algorithms = []
    for grid in grids:
        print(grid)
        classpath = grid['algorithm']
        if 'hyperparameters' in grid:
            hp_grid = grid['hyperparameters']
            for hyperparameters in flatten_algorithm_grid(hp_grid):
                algorithms.append(load_algorithm(classpath, hyperparameters))
        else:
            algorithms.append(load_algorithm(classpath))

    return algorithms


def load_algorithm(classpath, **hyperparameters):
    module_name, class_name = classpath.rsplit(".", 1)
    module = importlib.import_module(module_name)
    cls = getattr(module, class_name)
    instance = cls(**hyperparameters)
    return instance


def flatten_algorithm_grid(algorithm_grid):
    #    for hp in algorithm_grid:
    items = sorted(algorithm_grid.items())
    if not items:
        yield {}
    else:
        keys, values = zip(*items)
        for v in product(*values):
            params = dict(zip(keys, v))
            yield params
