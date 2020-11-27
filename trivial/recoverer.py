class Recoverer:
    def __init__(self, max_secret_value: int):
        self.max_secret_value = max_secret_value

    def recover(self, shares: list) -> int:
        secret = 0

        for i in shares:
            secret += i

        secret %= self.max_secret_value
        return secret
