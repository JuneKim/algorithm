## runtime: 87%, memory: 60.50%
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dic_alphabet = {}
        nums = [ord(ch) - 97 for ch in s]
        for idx, num in enumerate(nums):
            if num in dic_alphabet.keys():
                if idx - dic_alphabet[num] -1 != distance[num]:
                    return False
                
            else:
                dic_alphabet[num] = idx
        return True
    
data = [["abaccb", [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], ["aa", [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]]
results = [True, False]
is_success = True
    
sol = Solution()
for idx, _data in enumerate(data):
    ret = sol.checkDistances(_data[0], _data[1])
    if ret != results[idx]:
        is_success = False
        
        print (f"Failed: idx:{idx}")
        print (f"Outputs: {ret}")
        print (f"Expected: {results[idx]}")
        
if is_success:
    print ("Success!!") 
