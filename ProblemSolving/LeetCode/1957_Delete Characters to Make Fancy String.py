## runtime: 95.62%, memory: 54.25%
class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        wordCnt = 1
        prvCh = s[0]
        ret = prvCh
        for ch in s[1:]:
            if ch == prvCh:
                if wordCnt < 2:
                    ret = ret + ch
                wordCnt += 1
                
            else:
                prvCh = ch
                wordCnt = 1
                ret = ret + ch
        
        return ret
