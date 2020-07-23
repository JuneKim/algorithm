from typing import List
####################
#  0000000000000000
#  ->|     |<-
#   l_idx r_idx
####################

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l_idx = 0
        r_idx = len(height) -1
        while l_idx < r_idx:
            max_area = max(max_area, min(height[l_idx], height[r_idx]) * (r_idx - l_idx))
            if height[l_idx] > height[r_idx]:
                r_idx -= 1
            else:
                l_idx += 1
                
        return max_area
