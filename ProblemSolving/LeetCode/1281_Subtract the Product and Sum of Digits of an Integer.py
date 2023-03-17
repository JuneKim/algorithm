## runtime: 91.82%, memory: 42.49%
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = list(map(int, str(n)))
        product = 1
        for i in nums:
            product *= i
        sumNums = sum(nums)
        
        return product - sumNums
    
data = [234, 4421]
results = [15, 21]
is_success = True
    
sol = Solution()
for idx, _data in enumerate(data):
    ret = sol.subtractProductAndSum(_data)
    if ret != results[idx]:
        is_success = False
        
        print (f"Failed: idx:{idx}")
        print (f"Outputs: {ret}")
        print (f"Expected: {results[idx]}")
        
if is_success:
    print ("Success!!")
