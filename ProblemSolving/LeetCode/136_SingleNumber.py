class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for idx in range(0, len(nums), 2):
            if idx == len(nums) -1 or nums[idx] != nums[idx+1]:
                return nums[idx]
