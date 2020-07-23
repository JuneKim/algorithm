from typing import List
def permutation(nums: List[int]) -> List[List[int]]:
    data_len = len(nums)
    if data_len == 1:
        return [nums]
    
    ret_list = []
    for idx in range(data_len):
        tmp_list = permutation(nums[:idx] + nums[idx+1:])
        for tmp in tmp_list:
            sub_list = []
            sub_list.append(nums[idx])
            for sub_tmp in tmp:
                sub_list.append(sub_tmp)
            if not sub_list in ret_list:
                ret_list.append(sub_list)
            
    return ret_list
    
    
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return permutation(nums)  
