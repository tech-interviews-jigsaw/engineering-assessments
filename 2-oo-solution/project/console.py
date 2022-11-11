from store import store
from models.breed import Breed
from models.cow import Cow
from models.pen import Pen
from calculators.pen_calculator import PenCalculator

belgian = Breed(feed= 'hay', milk_amount=2, gas_amount=1, name = 'belgian blue')
braford = Breed(feed='leafs', milk_amount=5, gas_amount=3, name = 'braford')
angus = Breed(feed='grass', milk_amount=7, gas_amount=4, name = 'angus')

def build_n_cows_for(breed, n = 3):
    for i in range(n):
        cow = Cow(breed = breed)
        
for breed in store['breeds']:
    build_n_cows_for(breed)

for idx in range(len(store['breeds'])):
    pen = Pen(number = idx)
    breed = store['breeds'][idx]
    for cow in breed.cows:
        cow.pen = pen


pc = PenCalculator(store['pens'][0])