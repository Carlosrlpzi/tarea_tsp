import pytest

from tsp import Tour


def test_tour_closed(places):
    t1 = Tour()
    t1.append(places['A'])
    t1.append(places['B'])

    assert t1.closed == False

    t1.append(places['A'])

    assert t1.closed == True


def test_append_place(places):
    t1 = Tour()
    t1.append(places['A'])

    assert places['A'] == t1.initial

    assert t1.visited_places == set([places['A']])

    t1.append(places['B'])

    assert len(t1) == 2

    assert t1.visited_places == set([places['A'], places['B']])


def test_close_tour(places):
    t1 = Tour()
    t1.append(places['A'])

    t1.close()

    assert t1.closed == False

    t1.append(places['B'])

    t1.close()

    assert t1.closed == True

    assert t1.initial == t1.current

def test_missing(places):
    t1 = Tour()
    t2 = Tour()
    t1.append(palces['A'])
    t1.append(places['B'])
    t1.append(places['C'])

    t2.append(places['D'])

    assert t1.missing(places.values()) == set(t2._path)
