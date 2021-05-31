from main import move


def test_needs_to_move_to_north():
    given = (0, 0, 'N',)
    result = move(given)
    expected = (0, 1,'N',)

    assert result == expected


def test_needs_to_move_to_south():
    given = (0, 1, 'S',)
    result = move(given)
    expected = (0, 0, 'S',)

    assert result == expected


def test_needs_to_move_to_east():
    given = (0, 0, 'E',)
    result = move(given)
    expected = (1, 0, 'E',)

    assert result == expected


def test_needs_to_move_to_west():
    given = (1, 0, 'W',)
    result = move(given)
    expected = (0, 0, 'W',)

    assert result == expected
