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
    @settings(max_examples=10)
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
    @settings(max_examples=10)
    def test_is_even(x):
        assert R0102.is_even(x) == (x % 2 == 0)


class R0103:
    @staticmethod
    def minmax(arr):
        if len(arr) == 0:
            return (None, None)

        smallest = arr[0]
        largest = arr[0]

        if (len(arr)) == 1:
            return (smallest, largest)

        for value in arr:
            if value < smallest:
                smallest = value

            if value > largest:
                largest = value

        return (smallest, largest)

    @staticmethod
    @given(arr=st.lists(st.integers()))
    @settings(max_examples=10)
    def test_minmax(arr):
        # I handle arrays of length zero, but min/max don't
        assume(len(arr) > 1)
        assert R0103.minmax(arr) == (min(arr), max(arr))


class R0104:
    @staticmethod
    def sum_squares_less_than_n(n):
        total = 0

        while n > 0:
            total += n * n
            n -= 1

        return total

    @staticmethod
    @given(n=st.integers())
    @settings(max_examples=10)
    def test_sum_squares_less_than_n(n):
        # We don't have all day!
        assume(n < 10000)
        assert isinstance(R0104.sum_squares_less_than_n(n), int)
        assert R0104.sum_squares_less_than_n(n) >= 0


if __name__ == "__main__":
    R0101.test_is_multiple()
    R0102.test_is_even()
    R0103.test_minmax()
    R0104.test_sum_squares_less_than_n()
