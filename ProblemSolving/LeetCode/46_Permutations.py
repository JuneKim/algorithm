def deep_copy(nums: List[int]) -> List[int]:
    tmp_list = []
    for num in nums:
        tmp_list.append(num)
    return tmp_list

def permutation(nums: List[int]) -> List[List[int]]:
    if len(nums) == 1:
        return [nums]
    
    ret_list = []
    for idx in range(len(nums)):
        tmp_list = permutation(nums[0:idx] + nums[idx+1:])
        for tmp in tmp_list:
            sub_list = []
            sub_list.append(nums[idx])
            for item in tmp:
                sub_list.append(item)
            ret_list.append(sub_list)
        
    return ret_list 

#Permutation of [1,2,3] = List of [1 + Permutation[2,3]], 
#[2 + Permutation[1,3]], [3 + Permutation[1,2]]
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return permutation(nums) 
