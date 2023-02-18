## Runtime: 81.73%, Memory: 59.62%
## O(n) = n
class Solution:
    def minOperations(self, s: str) -> int:
        n_str = len(s)
        if n_str == 0: return
        n_min = 999999

        init_val = s[0]
        for _ in range(2):
            init_val = '0' if init_val == '1' else '1'
            n_cnt = 1 if s[0] != init_val else 0
            tmp_ch = init_val
            for ch in s[1:]:
                if tmp_ch == ch:
                    n_cnt += 1
                    tmp_ch = '0' if ch == '1' else '1'
                else:
                    tmp_ch = ch
            if n_min > n_cnt:
                n_min = n_cnt

        return n_min
