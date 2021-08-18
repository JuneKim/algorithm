class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        _half = int(x/2)
        _candidate = 0
        for i in range(0, _half+1):
            if i*i <= x:
                _candidate = i
            else:
                break
            
        return _candidate

# Test Code
import sys
test_input = [1, 2, 3, 4, 5, 7, 10]
answers = [1, 1, 1, 2, 2, 2, 3]
s = Solution()
for _idx, _data in enumerate(test_input):
    if answers[_idx] != s.mySqrt(_data):
        print (f"Error: The answer of {_data} should be {answers[_idx]}")
        sys.exit(1)

print ("Success")
