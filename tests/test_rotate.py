from main import rotate
from pytest import fixture

@fixture(scope='function')
def sibling_orientation():
    return {
        'N': 'W',
        'E': 'N',
        'S': 'E',
        'W': 'S',
    }

def test_needs_to_turn_left(sibling_orientation):
    for old, new in sibling_orientation.items():
        coordinates = (0,0,old,)
        result = rotate(coordinates, 'L')
        expected = (0, 0, new,)

        assert result == expected


def test_needs_to_turn_right(sibling_orientation):
    for new, old in sibling_orientation.items():
        coordinates = (0,0,old,)
        result = rotate(coordinates, 'R')
        expected = (0, 0, new,)

        assert result == expected
