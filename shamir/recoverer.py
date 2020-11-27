from utils.math_operations import lagrange_interpolate


class Recoverer:
    def __init__(self, prime_number: int):
        self.prime_number = prime_number

    def recover(self, shares: list) -> int:
        secret = 0

        x_values, y_values = zip(*shares)
        return lagrange_interpolate(0, x_values, y_values, self.prime_number)
