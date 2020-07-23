class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._min = 99999999999999
        self._data = []
               

    def push(self, x: int) -> None:
        self._data.append(x)
        if self._min > x:
            self._min = x

    def pop(self) -> None:
        tmp = self._data.pop()
        if tmp == self._min:
            tmp = 99999999999999
            for i in self._data:
                if i < tmp:
                    tmp = i
                    
            self._min = tmp
        
    def top(self) -> int:
        return self._data[-1]

    def getMin(self) -> int:
        return self._min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
