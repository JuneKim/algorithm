## runtime: 41.5#%, memory: 5.56%
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        strNums = [str(i) for i in range(left, right+1)]
        li_ret = []
        for strNum in strNums:
            target = int(strNum)
            is_found = True
            for ch in strNum:
                if int(ch) == 0 or target % int(ch) != 0:
                    is_found = False
                    break
            if is_found:
                li_ret.append(target)
        return li_ret
    
## runtime: 43.53%, memory: 59.85%
class Solution2:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        li_ret = []
        for target in range(left, right+1):
            nums = [*str(target)]
            is_found = True
            for num in nums:
                if int(num) == 0 or target % int(num) != 0:
                    is_found = False
                    break
            if is_found:
                li_ret.append(target)
        return li_ret
      
data = [[1, 22], [47,85]]
results = [[1,2,3,4,5,6,7,8,9,11,12,15,22], [48,55,66,77]]
is_success = True
    
sol = Solution()
for idx, _data in enumerate(data):
    ret = sol.selfDividingNumbers(_data[0], _data[1])
    if ret != results[idx]:
        is_success = False
        
        print (f"Failed: idx:{idx}")
        print (f"Outputs: {ret}")
        print (f"Expected: {results[idx]}")
        
if is_success:
    print ("Success!!")
