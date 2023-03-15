# runtime: 75.23%, memory: 49.30%
import numpy
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        
        myArr = [[] for _ in range(len(grid[0]))]
        for idx, ele in enumerate(grid):
            ele.sort()
            
            ## can be replaced by numpy.transpose
            for idy, num in enumerate(ele):
                myArr[idy].append(num)
        
        mySum = 0
        for idx, ele in enumerate(myArr):
            mySum += max(ele)
        
        return mySum
        
    
data = [[[1,2,4],[3,3,1]], [[10]]]
results = [8, 10]
is_success = True
    
sol = Solution()
for idx, _data in enumerate(data):
    ret = sol.deleteGreatestValue(_data)
    if ret != results[idx]:
        is_success = False
        
        print (f"Failed: idx:{idx}")
        print (f"Outputs: {ret}")
        print (f"Expected: {results[idx]}")
        
if is_success:
    print ("Success!!")
