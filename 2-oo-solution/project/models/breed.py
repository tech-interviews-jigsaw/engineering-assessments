from store import store

class Breed:
    FEEDS = ['grass', 'corn', 'hay', 'leafs']

    def __init__(self, name: str, feed: str, milk_amount: int, gas_amount: int) -> 'Breed':
        store['breeds'].append(self)
        if feed not in self.FEEDS:
            raise ValueError(f"feed: {feed} not in {self.FEEDS}")
        self.name = name
        self.feed_type = feed
        self.milk_amount = milk_amount
        self.gas_amount = gas_amount

    @property
    def cows(self) -> list:
        return [cow for cow in store['cows'] if cow.breed == self]

    @property
    def pens(self) -> list:
        return [pen for pen in store['pens'] if pen.breed == self]