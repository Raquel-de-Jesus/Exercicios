from coordenate import Coordinate
from quadrant import Quadrant


def test_should_get_quadrant_coordinate():
    # Arrange / Setup
    a = -8
    b = -1
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "Third"
