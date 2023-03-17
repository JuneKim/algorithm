## Runtime: 99.12%, Memory: 12.35%
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        nums = [0 if ch == "W" else 1 for ch in blocks]
        if len(blocks) < k:
            return -999
        
        smallCnt = k
        cnt = 0
        for idx in range(len(nums) - k +1):
            #print (nums[idx:idx+k])
            if idx == 0:
                cnt = sum(nums[idx:idx+k])
            else:
                cnt = cnt + nums[idx+k-1] - nums[idx-1]
                
            if k - cnt < smallCnt:
                smallCnt = k - cnt
                #print (f"{idx}:{smallCnt}")
                
        return smallCnt
    
data = [["WBBWWBBWBW", 7], ["WBWBBBW", 2]]
results = [3, 0]
is_success = True
    
sol = Solution()
for idx, _data in enumerate(data):
    ret = sol.minimumRecolors(_data[0], _data[1])
    if ret != results[idx]:
        is_success = False
        
        print (f"Failed: idx:{idx}")
        print (f"Outputs: {ret}")
        print (f"Expected: {results[idx]}")
        
if is_success:
    print ("Success!!") 
