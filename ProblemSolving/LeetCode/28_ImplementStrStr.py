class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ret = -1
        if needle == "":
            return 0
        
        if needle in haystack:
            prefixs = haystack.split(needle)
            ret = len(prefixs[0])
            
        return ret
