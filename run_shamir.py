import random

from shamir.recoverer import Recoverer
from shamir.splitter import Splitter
from utils.math_operations import generate_prime_number

MIN_VALUE = 900
MAX_VALUE = 1000

shares_number = 6
threshold = 3
secret = 10


def shamir_method():
    prime_number = generate_prime_number(MIN_VALUE, MAX_VALUE)

    splitter = Splitter(prime_number)
    recoverer = Recoverer(prime_number)

    shares = splitter.split_secret(secret, shares_number, threshold)
    chosen_shares = [shares[0], shares[2], shares[4]]
    print(shares)
    print(chosen_shares)
    print(secret)

    recovered_secret = recoverer.recover(chosen_shares)

    print(recovered_secret)


shamir_method()
