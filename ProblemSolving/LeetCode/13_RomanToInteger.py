values = {'I': 1, "X": 10,"V": 5, "L": 50, "C": 100, "D": 500, "M": 1000}
reduced = {"V": 4, "X": 9, "L": 40, "C": 90, "D": 400, "M": 900}


class Solution:
    def romanToInt(self, s: str) -> int:
        ret = 0
        for idx in range(len(s)):
            if idx != 0:
                if s[idx-1] == 'I' and (s[idx] == 'V' or s[idx] == 'X'):
                    ret += reduced[s[idx]] -1
                elif s[idx-1] == 'X' and (s[idx] == 'L' or s[idx] == 'C'):
                    ret += reduced[s[idx]] -10
                elif s[idx-1] == 'C' and (s[idx] == 'D' or s[idx] == 'M'):
                    ret += reduced[s[idx]] - 100
                else:
                    ret += values[s[idx]]
            else:
                ret = ret + values[s[idx]]
            
        return ret
            
