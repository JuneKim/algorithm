from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        max_cnt = 0
        max_num = 0
        for i in nums:
            if str(i) in counts.keys():
                counts[str(i)] += 1
                
            else:
                counts[str(i)] = 1
            
            if counts[str(i)] > max_cnt:
                max_cnt = counts[str(i)]
                max_num = i
        
        return max_num

sol = Solution()
sol.majorityElement([3,3,4])