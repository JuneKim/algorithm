from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        tmp = []
        _n = len(matrix)
        for idx1 in range(_n):
            _tmp_list = []
            for idx2 in range(_n - 1, -1, -1):
                _tmp_list.append(matrix[idx2][idx1])
            tmp.append(_tmp_list)
        #matrix = tmp 
        for _idx1 in range(_n):
            matrix[_idx1] = tmp[_idx1]


inData = [[1,2,3], [4,5,6], [7,8,9]] 
sol = Solution()
sol.rotate(inData)
print (inData)
	
