from models.pen import Pen
import numpy as np
class PenCalculator:
    def __init__(self, pen):
        self.pen = pen

    def number_of_cows(self):
        return len(self.pen.cows)

    def milk(self):
        milk_amnt = self.pen.breed.milk_amount
        return milk_amnt*self.number_of_cows()

    def greenhouse_gas(self):
        gas_amnt = self.pen.breed.gas_amount
        return gas_amnt*self.number_of_cows()

# add capacity constraint
# look up influences of 