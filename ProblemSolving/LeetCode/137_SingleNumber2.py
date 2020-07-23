from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        calculated = {}
        for num in nums:
            if num in calculated.keys():
                calculated[num] += 1
            else:
                calculated[num] = 1
        for key, val in calculated.items():
            if val == 1:
                return key
        
        return 0
