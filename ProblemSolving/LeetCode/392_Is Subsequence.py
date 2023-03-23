## runtime: 97.41%, memory: 32.5%
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idt = 0
        is_found = True
        for ids, chs in enumerate(s):
            if chs in t[idt:]:
                idt = idt + t[idt:].index(chs) + 1
                if ids < len(s) - 1 and idt > len(t) - 1:
                    is_found = False
                    
                    break
            else:
                is_found = False
                break
                
        return is_found
    
data = [["abc", "ahbgdc"], ["axc", "ahbgdc"]]
result = [True, False]
sol = Solution()
is_success = True
for _idx, _data in enumerate(data):
    ret = sol.isSubsequence(_data[0], _data[1])
    if result[_idx] != ret:
        print (f"Failed. {_idx}")
        print (f"Output:{ret}")
        print (f"Expected:{result[_idx]}")        
        is_success = False
        
if is_success:
    print ("Success!!")
