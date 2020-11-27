from trivial.recoverer import Recoverer
from trivial.splitter import Splitter

MAX_VALUE = 1000
shares_number = 5
secret = 456


def trivial_method():
    splitter = Splitter(MAX_VALUE)
    recoverer = Recoverer(MAX_VALUE)

    shares = splitter.split_secret(secret, shares_number)
    recovered_secret = recoverer.recover(shares)

    print(shares)
    print(secret)
    print(recovered_secret)


trivial_method()
