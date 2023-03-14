## runtime: 90.73%, memory: 96%
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        totalSum = sum(arr)
        totalLen = len(arr)
        partSum = totalSum // 3
        remainder = totalSum % 3
        if remainder > 0:
            return False

        sumx = 0
        for idx, val in enumerate(arr):
            sumx += val
            if sumx == partSum:
                break
        sumy = 0
        for idy, val in enumerate(arr[-1::-1]):
            sumy += val
            if sumy == partSum:
                break

        print (idx, totalLen - idy -1)
        if idx == totalLen - 1 or idy == totalLen - 1 or idx + idy >= totalLen - 2:
            return False

        return True
    
    #if sum(arr) % 3 != 0:
    #    return False
    #count, partSum, target = 0, 0, sum(arr) // 3
    #for i in arr:
    #    partSum += i
    #    if partSum == target:
    #        count += 1
    #        partSum = 0
        
    #return count >=3
    
    
data = [[0,2,1,-6,6,-7,9,1,2,0,1],[0,2,1,-6,6,7,9,-1,2,0,1], [3,3,6,5,-2,2,5,1,-9,4], [6,1,1,13,-1,0,-10,20], [0,0,0,0], [1, -1, 1, -1]]
results = [True, False, True, False, True, False]
is_success = True
    
sol = Solution()
for idx, _data in enumerate(data):
    ret = sol.canThreePartsEqualSum(_data)
    if ret != results[idx]:
        is_success = False
        
        print (f"Failed: idx:{idx}")
        print (f"Outputs: {ret}")
        print (f"Expected: {results[idx]}")
        
if is_success:
    print ("Success!!")
