braces = {'}': "{", "]": "[", ")": "("}

class Stack:
    def __init__(self):
        self._data = []
    
    def push(self, data: str):
        self._data.append(data)
    def pop(self) -> str:
        if len(self._data) > 0:
            return self._data.pop()
        else:
            return ""
    def __len__(self):
        return len(self._data)

class Solution:
    def isValid(self, s: str) -> bool:
        self._stack = Stack()
        for ch in s:
            if ch in braces.keys():
                prev = self._stack.pop()
                if prev != braces[ch]:
                    return False
            else:
                self._stack.push(ch)
        
        if len(self._stack) == 0:
            return True
        return False
