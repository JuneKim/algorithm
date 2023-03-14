class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
          
        ## sort
        nums.sort()
        trials = k

        ### case 1 len (negative) >= k:
        for idx, num in enumerate(nums):
            if trials > 0 and num < 0:
                nums[idx] = -num
                trials -= 1
            else:
                break

        # only when trial is odd
        if trials > 0 and trials % 2 == 1:
            # resort
            nums.sort()
            nums[0] = -nums[0]

        return sum(nums)
        
    def largestSumAfterKNegations2(self, nums: List[int], k: int) -> int:
      for _ in range(k):
        idx = nums.index(min(nums))
        nums[idx] = -nums[idx]
      
      return sum(nums)
    
data = [[[5,6,9,-3,3], 2],]
results = [20]
is_success = True

sol = Solution()
for idx, _data in enumerate(data):
    ret = sol.largestSumAfterKNegations(_data[0], _data[1])
    if ret != results[idx]:
        is_success = False
        
        print (f"Failed: idx:{idx}")
        print (f"Outputs: {ret}")
        print (f"Expected: {results[idx]}")
        
if is_success:
    print ("Success!!")
    
    
    
