class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # find shortest
        if len(strs) == 0:
            return ""
        
        short_len = 999999
        short_str = ""
        for s in strs:
            if len(s) < short_len:
                short_len = len(s)
                short_str = s
        
        diff = 0
        ret = str()
        for idx in range(short_len):
            
            for s in strs:
                if short_str[idx] != s[idx]:
                    diff = 1
                    break
                    
            if diff == 1:
                break
            else:
                ret += short_str[idx]
                
            
        return ret
