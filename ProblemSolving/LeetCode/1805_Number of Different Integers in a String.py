## runtime: 51.67%, memory: 95.19%
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        li_ret = re.findall(r"\d+", word)
        #return len(set([int(s) for s in li_ret]))
        return len(set(map(int, li_ret)))
        

data = ["a123bc34d8ef34", "leet1234code234", "a1b01c001", "gi851a851q8510v"]
result = [3, 2, 1, 2]
sol = Solution()
is_success = True
for _idx, _data in enumerate(data):
    ret = sol.numDifferentIntegers(_data)
    if result[_idx] != ret:
        print (f"Failed. {_idx}")
        print (f"Output:{ret}")
        print (f"Expected:{result[_idx]}")        
        is_success = False
        
if is_success:
    print ("Success!!")
