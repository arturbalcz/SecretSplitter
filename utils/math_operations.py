import sympy


def function_value(x, coefficients, mod):
    sum = 0
    for i in range(1, len(coefficients)):
        sum += coefficients[i] * (x ** i)

    value = (coefficients[0] + sum) % mod
    return value


def generate_prime_number(min_value, max_value):
    return sympy.randprime(min_value, max_value)


def lagrange_interpolate(x, arguments, values, mod):
    numerators = []
    denominators = []
    for i in range(len(arguments)):
        others = list(arguments)
        current = others.pop(i)
        numerators.append(product(x - o for o in others))
        denominators.append(product(current - o for o in others))
    denominator = product(denominators)
    numerator = sum([division_modulo(numerators[i] * denominator * values[i] % mod, denominators[i], mod)
                     for i in range(len(arguments))])
    return (division_modulo(numerator, denominator, mod) + mod) % mod


def division_modulo(dividend, divider, mod):
    inverse, _ = extended_gcd(divider, mod)
    return dividend * inverse


def extended_gcd(a, b):
    x = 0
    last_x = 1
    y = 1
    last_y = 0
    while b != 0:
        quotient = a // b
        a, b = b, a % b
        x, last_x = last_x - quotient * x, x
        y, last_y = last_y - quotient * y, y
    return last_x, last_y


def product(values):
    accumulator = 1
    for v in values:
        accumulator *= v
    return accumulator
