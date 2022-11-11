from store import store
class Cow:
    def __init__(self, breed):
        store['cows'].append(self)
        self._pen = None
        self.breed = breed
    
    @property
    def pen(self):
        return self._pen

    @pen.setter
    def pen(self, pen):
        self._pen = pen

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, breed):
        self._breed = breed