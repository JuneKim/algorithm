## 62.2%, memory: 46.13%
class Solution:
    ## A :1 Z: 26
    def titleToNumber(self, columnTitle: str) -> int:
        nums = [ord(ch) - 64 for ch in columnTitle] ## O(n)
        mySum = 0
        pos = 1
        for num in nums[::-1]: ## O(n)
            mySum += num*pos
            pos *= 26
        return mySum
    
data = ["A", "AB", "ZY"]
results = [1, 28, 701]
is_success = True
    
sol = Solution()
for idx, _data in enumerate(data):
    ret = sol.titleToNumber(_data)
    if ret != results[idx]:
        is_success = False
        
        print (f"Failed: idx:{idx}")
        print (f"Outputs: {ret}")
        print (f"Expected: {results[idx]}")
        
if is_success:
    print ("Success!!")
