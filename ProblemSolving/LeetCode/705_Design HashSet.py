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

    
## runtime: 85.83%, 57.33%
class MyHashSet2:
    
    def eval_hash(self, key):
        return ((key*1031237) & (1<<20) - 1)>>5

    def __init__(self):
        self.arr = [[] for _ in range(1<<15)]

    def add(self, key: int) -> None:
        t = self.eval_hash(key)
        if key not in self.arr[t]:
            self.arr[t].append(key)

    def remove(self, key: int) -> None:
        t = self.eval_hash(key)
        if key in self.arr[t]:
            self.arr[t].remove(key)

    def contains(self, key: int) -> bool:
        t = self.eval_hash(key)
        return key in self.arr[t]
