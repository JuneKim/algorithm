class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.findmedian(nums, target, 0)
        
        
    def findmedian(self, nums: List[int], target: int, idx: int) -> int:
        if len(nums) < 3:
            if len(nums) == 0:
                return -1
            
            if nums[0] == target:
                return idx
            elif len(nums) == 2 and nums[1] == target:
                return idx+1
            
            return -1
        
        median_idx = (len(nums)+1)//2 - 1
        median = nums[median_idx]
        if median == target:
            return median_idx + idx
        
        elif median < target:
            return self.findmedian (nums[median_idx + 1:], target, idx + median_idx + 1)
        
        else:
            return self.findmedian (nums[:median_idx], target, idx)
