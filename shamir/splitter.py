import random

import sympy as sympy

from utils.math_operations import function_value


class Splitter:
    def __init__(self, prime_number: int):
        self.prime_number = prime_number

    def split_secret(self, secret: int, shares_number: int, threshold: int) -> list:
        if secret >= self.prime_number or shares_number >= self.prime_number:
            raise Exception("Secret value is bigger than declared Max Value: {}".format(self.prime_number))

        coefficients = random.choices(range(0, self.prime_number - 1), k=threshold - 1)
        coefficients.insert(0, secret)
        shares = []
        points = random.sample(range(1, self.prime_number), k=shares_number)
        for i in points:
            share = function_value(i, coefficients, self.prime_number)
            shares.append((i, share))

        return shares
