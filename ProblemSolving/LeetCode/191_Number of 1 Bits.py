class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        tmp_cnt = n
        while tmp_cnt != 0:
            if tmp_cnt & 1 == 1:
                cnt += 1
            tmp_cnt = tmp_cnt >> 1
                
        return cnt
    
        """
        :type n: int
        :rtype: int
        """
        #return bin(n).count("1")
