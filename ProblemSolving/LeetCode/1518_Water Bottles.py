# runtime: 43.85%, memory: 96.43%
class Solution1:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drinks = 0
        full = numBottles
        while full >= numExchange:
            drinks += numExchange
            full = full - numExchange + 1

        return drinks + full

## runtime: 72.55%, memory: 47.24%
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drinks = 0
        full = numBottles
        while full >= numExchange:
            newBottle = full // numExchange
            remainder = full % numExchange
            drinks += (full - remainder)
            full = remainder + newBottle

        return drinks + full

    
    
data = [[9,3], [15,4]]
results = [13, 19]
is_success = True
    
sol = Solution()
for idx, _data in enumerate(data):
    ret = sol.numWaterBottles(_data[0], _data[1])
    if ret != results[idx]:
        is_success = False
        
        print (f"Failed: idx:{idx}")
        print (f"Outputs: {ret}")
        print (f"Expected: {results[idx]}")
        
if is_success:
    print ("Success!!")
