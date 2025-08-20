from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import MagicMock

mock = Mock()
mock.get.return_value = "abc"
print(mock.get())

magic_mock = MagicMock()
magic_mock.__str__.return_value = "abc"
print(magic_mock)

def foo():
    return "abc"

with patch("__main__.foo") as mock_foo:
    mock_foo.return_value = 123
    print(foo())

@patch("__main__.foo")
def test_foo(mock_foo):
    mock_foo.return_value = 123
    print(foo())

test_foo()