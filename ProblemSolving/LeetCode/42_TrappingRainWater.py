from typing import List
#
# 1. Find max of height
# 2. if num of max is larger than 1:
# 2-1. calculate inner area
# 3. add area on left and right sides
#          |         |
#    |     |         |     |
#    |     |         |     |
#     left    inner    right
###############################

def cal_water(height: List[int]) -> int:
    l_idx = 0
    r_idx = 1
    if len(height) is 0:
        return 0
    total_water = 0
    contained = 0
    
    while r_idx < len(height):
        if height[r_idx] >= height[l_idx]:
            total_water += contained
            contained = 0
            l_idx = r_idx
        else:
            contained += (height[l_idx] - height[r_idx])
        r_idx += 1
        
    return total_water

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        
        find_max = max(height)
        
        if find_max is 0:
            return 0
        
        water = 0
        max_list = []
        for idx in range(len(height)):
            if find_max == height[idx]:
                max_list.append(idx)
                
        if len(max_list) > 1: # more than 2
            prev = max_list[0]
            for idx in max_list[1:]:
                for inner in range(prev, idx):
                    water += (find_max - height[inner])
                
                prev = idx

            lidx = max_list[0]
            ridx = max_list[-1]
        else:
            lidx = max_list[0]
            ridx = max_list[0]
                       
        if lidx is not 0:
            water += cal_water(height[:lidx+1])
                
        if ridx is 0:
            water += cal_water(height[::-1])
        elif ridx is not len(height) -1:
            water += cal_water(height[-1:ridx-1: -1])
            
        return water
                       
sol = Solution()
ret = sol.trap([4,2,0,3,2,4,3,4])
print (ret)
    
        