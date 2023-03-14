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
