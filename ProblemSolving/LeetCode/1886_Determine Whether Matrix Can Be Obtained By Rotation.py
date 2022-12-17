class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # 90 degree: M(i,j) -> M(j, N-j)
        N = len(mat)-1
        # 90 degree

        tmp_mat = mat
        while True:
            tmp_mat = self.rotation90(tmp_mat)
            if tmp_mat == target:
                return True
            
            if tmp_mat == mat:
                break
        
        return False

        # import copy
        # copy.deepcopy()
    def rotation90(self, prev_mat: List[List[int]]) -> List[List[int]]:
        # 90 degree: M(i,j) -> M(j, N-j)
            
        N = len(prev_mat)-1
        # O(n^2)
        li_ret = [[0 for _ in range(N+1)] for _ in range(N+1)]
        for i, row in enumerate(prev_mat):
            for j, col in enumerate(row):
                # 90 degree / 180 degree / 270 degree
                li_ret[j][N-i] = col

        return li_ret
