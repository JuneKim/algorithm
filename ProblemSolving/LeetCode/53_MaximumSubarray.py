class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = nums[0]
        tmp_val = 0
        max_item = nums[0]
        for num in nums:
            tmp_val += num
            if tmp_val <= 0:
                tmp_val = 0
            elif tmp_val > max_val:
                max_val = tmp_val
            
            if num > max_item:
                max_item = num
                
        if max_item > max_val:
            return max_item
        
        return max_val
