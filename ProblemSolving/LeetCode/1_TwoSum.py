from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data_len = len(nums)
        for idx1 in range(data_len):
            for idx2 in range(idx1 + 1, data_len):
                if nums[idx1] + nums[idx2] == target:
                    return [idx1, idx2]
                
        return []
