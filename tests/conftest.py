import io

import pytest

from tsp import TSP, Place, Tour


@pytest.fixture
def coordinates_file():

    coordinates = """
    0 0
    1 0
    0 1
    1 1
    2 3
    """

    return io.StringIO(coordinates)


@pytest.fixture
def distances_file():

    distances = """
    0.0  3.0  4.0  2.0  7.0
    3.0  0.0  4.0  6.0  3.0
    4.0  4.0  0.0  5.0  8.0
    2.0  6.0  5.0  0.0  6.0
    7.0  3.0  8.0  6.0  0.0
    """

    return io.StringIO(distances)


@pytest.fixture
def tsp_obj(coordinates_file, distances_file):
    return TSP.from_files(coordinates_file, distances_file)


@pytest.fixture
def tour_obj():
    t = Tour()

    t.append(Place(0, 0, 0))
    t.append(Place(1, 1, 0))
    t.append(Place(3, 1, 1))
    t.append(Place(2, 0, 1))
    t.append(Place(4, 2, 3))
    t.close()

    return t


@pytest.fixture
def places():
    return {
        'A': Place('A', 0, 0),
        'B': Place('B', 1, 0),
        'C': Place('C', 0, 1),
        'D': Place('D', 1, 1)
    }
