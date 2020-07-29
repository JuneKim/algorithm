from typing import List

subset_list = []
def get_subset(nums: List[int], onoff: List[int], n:int, depth:int):
    if n == depth:
        tmp_list = []
        for idx in range(n):
            if onoff[idx] == 1:
                tmp_list.append(nums[idx])
        subset_list.append(tmp_list)
        return
    
    onoff[depth] = 1
    get_subset(nums, onoff, n, depth+1)
    onoff[depth] = 0
    get_subset(nums, onoff, n, depth+1)


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        onoff = []
        if nums == []:
            return []

        global subset_list
        subset_list = []
        
        data_len = len(nums)
        for _ in range(data_len):
            onoff.append(0)
        print (len(onoff))
        get_subset(nums, onoff, data_len - 1, 0)
        return subset_list
     

sol = Solution()
print (sol.subsets([1,2,3]))my