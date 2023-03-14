## runtime: 67.27%, memory: 9.65
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        if len(num) == 0:
            return k
        
        conv_num = int("".join([str(i) for i in num]))
        return [int (ch) for ch in str(conv_num + k)]
        
        
data = [[[1,2,0,0], 34], [[2,7,4], 181], [[2,1,5], 806] ]
output = [[1,2,3,4], [4,5,5], [1,0,2,1]]

sol = Solution()
is_success = True
for _idx, _data in enumerate(data):
    #print (type(_data))
    #print (_data[0])
    #print (_data[1])
    ret = sol.addToArrayForm(_data[0], _data[1])
    if ret != output[_idx]:
        print (f"Failed: idx:{_idx}")
        print (f"Output: {ret}")
        print (f"Expected: {output[_idx]}")
        is_success = False
        
if is_success:
    print ("Success!!")
