import pytest
from calculator import add

# Test data jo CSV ya external resource se map hota hai
test_data = [
    (2, 3, 5),
    (10, 5, 15),
    (-2, 2, 0),
    (0, 0, 0)
]

@pytest.mark.parametrize("a, b, expected", test_data)
def test_add_parameterized(a, b, expected):
    assert add(a, b) == expected