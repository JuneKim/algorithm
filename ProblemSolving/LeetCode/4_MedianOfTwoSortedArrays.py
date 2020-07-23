from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tmp_list = nums1 + nums2
        tmp_list.sort()
        medi = int(len(tmp_list)/2)
        if len(tmp_list) % 2 == 0:
            
            return (tmp_list[medi -1] + tmp_list[medi]) / 2.0
        else:
            return tmp_list[medi]
