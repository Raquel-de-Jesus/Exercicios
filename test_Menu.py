from menu import Menu
from coordenate import Coordinate


def test_should_coordinate_is_valid():
    # Arrange / Setup
    a = 10
    b = 5

    coordinates = Coordinate(a, b)
    menu = Menu()
    
    # Act / Action
    result = menu.cordinate_is_valid(coordinates)

    # Assert
    assert result == True
