from store import store
from models.cow import Cow
class Pen:
    def __init__(self, number: int) -> "Pen":
        store['pens'].append(self)
        self.number = number

    @property
    def cows(self):
        return [cow for cow in store['cows'] if cow.pen == self]

    @property
    def breed(self):
        if self.cows:
            return self.cows[0].breed

    def add_cow(self, cow: Cow) -> "Pen":
        if self.breed and self.breed != cow.breed:
            raise ValueError(f"The cow's breed ({cow.breed}) must be same as pen breed: ({self.breed})")
        cow.pen = self
        return self

    

    