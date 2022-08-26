class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordlist = s.split(" ")
        idx = -1
        
        while wordlist[idx] is "":
            idx -= 1
            
        return len(wordlist[idx])
        
