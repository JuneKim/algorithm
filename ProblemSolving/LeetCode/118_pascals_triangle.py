class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows is 1:
            return [[1]]

        def retPascal(curr_num, prev_list):
            tmp_list = [1]
            for idx, val in enumerate(prev_list):
                if idx is not len(prev_list)-1:
                    tmp_list.append(prev_list[idx] + prev_list[idx+1])
            tmp_list.append(1)
            return tmp_list
        result_list = [[1]]    
        for idx in range(2, numRows + 1):
            prev_list = result_list[-1]
            result_list.append(retPascal(idx, prev_list))
            
        return result_list
                
