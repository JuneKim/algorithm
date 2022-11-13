class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True
        
        mydiff = 0
        for idx, num in enumerate(nums):
            if idx == 0:
                continue
                
            diff = num - nums[idx - 1]
            if mydiff == 0:
                mydiff = diff
                continue
            
            if diff == 0:
                continue
                
            if diff*mydiff < 0:
                return False                
                    
        return True
 
## or
# if len(nums) == 1:
#   return True
# sorted = sort(nums)
# if sorted == nums or sorted == nums[::-1]:
#   return True
# else:
#   return False
