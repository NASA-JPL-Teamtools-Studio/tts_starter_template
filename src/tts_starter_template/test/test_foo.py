import pytest

from tts_starter_template.foo import Foo


class TestFoo:
    """Test for class Foo"""

    @pytest.mark.parametrize(
        "input_1, input_2, expected",
        [
            # 1 + 1 = 2
            (1, 1, 2),
            # None for input_2 defaults to 1, 5 + 1 = 6
            (5, None, 6),
        ],
    )
    def test_bar(self, input_1, input_2, expected):
        """Test for method bar"""
        foo = Foo(input_1, input_2)

        result = foo.bar()
        assert expected == result
