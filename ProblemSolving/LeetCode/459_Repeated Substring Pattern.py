import re
## runtime: 18.82%, memory: 7.13%
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        subsets = re.findall(r"^(\w+)\1+$", s)
        return len(subsets) > 0           
    
data = ["abab", "aba", "abcabcabcabc"]
result = [True, False, True]
sol = Solution()
is_success = True
for _idx, _data in enumerate(data):
    ret = sol.repeatedSubstringPattern(_data)
    if result[_idx] != ret:
        print (f"Failed. {_idx}")
        print (f"Output:{ret}")
        print (f"Expected:{result[_idx]}")        
        is_success = False
        
if is_success:
    print ("Success!!")
