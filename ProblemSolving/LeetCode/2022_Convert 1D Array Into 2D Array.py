class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        myresult = []
        curr_idx = 0
        if len(original) != m*n:
            return []

        start_idx = 0
        for _ in range(m):           
            myresult.append(original[start_idx:start_idx + n])
            start_idx += n

        return myresult
