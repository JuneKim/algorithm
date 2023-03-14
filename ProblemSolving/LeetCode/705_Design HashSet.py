# runtime: 19.33%, memory: 91.43%
class MyHashSet:

    def __init__(self):
        self._hashset = []        

    def add(self, key: int) -> None:
        if key in self._hashset:
            self._hashset.remove(key)

        self._hashset.append(key)        

    def remove(self, key: int) -> None:
        if key in self._hashset:
            self._hashset.remove(key)

    def contains(self, key: int) -> bool:
        if key in self._hashset:
            return True
        
## runtime: 85.83%, 57.33%
class MyHashSet1:

    def __init__(self):
        self._hashset = set()       

    def add(self, key: int) -> None:
        self._hashset.add(key)        

    def remove(self, key: int) -> None:
        # remove: raise an error if not exists. discard does not raise an error
        self._hashset.discard(key)

    def contains(self, key: int) -> bool:
        if key in self._hashset:
            return True

        return False
