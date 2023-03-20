## runtime: 86.36%, memory: 69.86%
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            # return [0] * len(code)
            return [0 for _ in code]
        
        if len(code) == 0:
            return []
        
        li_Ret = []
        if k > 0:
            code = code[1:] + [code[0]]
            #print (code)
        else:
            code = code[k:] + code[:k]
            #print (code)
            k = -k
            
        curr_sum = 0
        for idx in range(len(code)):
            if idx == 0:
                curr_sum = sum([code[(idx + idy)%len(code)] for idy in range(k)])
            else:
                curr_sum = curr_sum - code[idx-1] + code[(idx + k -1)%len(code)]
            
            li_Ret.append(curr_sum)
            
        return li_Ret
    
data = [[[5,7,1,4], 3], [[1,2,3,4], 0], [[2,4,9,3], -2]]
results = [[12,10,16,13], [0,0,0,0], [12,5,6,13]]
is_success = True
    
sol = Solution()
for idx, _data in enumerate(data):
    ret = sol.decrypt(_data[0], _data[1])
    if ret != results[idx]:
        is_success = False
        
        print (f"Failed: idx:{idx}")
        print (f"Outputs: {ret}")
        print (f"Expected: {results[idx]}")
        
if is_success:
    print ("Success!!") 
