from hypothesis import assume, given, settings, strategies as st


class R0101:
    @staticmethod
    def is_multiple(x, y):
        if x == 0 or y == 0:
            return False

        while x > y:
            x -= y

        return x == y

    @staticmethod
    @given(x=st.integers(), y=st.integers())
    @settings(max_examples=100)
    def test_is_multiple(x, y):
        assume(x != 0)
        assume(y != 0)
        assert R0101.is_multiple(x, y)


class R0102:
    @staticmethod
    def is_even(x):
        x = abs(x)

        while x > 0:
            x -= 2

        return x == 0

    @staticmethod
    @given(x=st.integers())
    @settings(max_examples=100)
    def test_is_even(x):
        assert R0102.is_even(x) == (x % 2 == 0)


if __name__ == "__main__":
    R0102.test_is_even()
