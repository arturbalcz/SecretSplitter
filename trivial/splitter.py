import random


class Splitter:
    def __init__(self, max_secret_value: int):
        self.max_secret_value = max_secret_value

    def split_secret(self, secret: int, shares_number: int) -> list:
        if secret >= self.max_secret_value:
            raise Exception("Secret value is bigger than declared Max Value: {}".format(self.max_secret_value))

        shares = random.choices(range(0, self.max_secret_value-1), k=shares_number - 1)
        last_share = secret

        for i in shares:
            last_share -= i

        last_share %= self.max_secret_value
        shares.append(last_share)
        return shares
