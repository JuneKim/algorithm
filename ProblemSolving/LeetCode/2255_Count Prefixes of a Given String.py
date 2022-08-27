class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        cnt = 0
        for idx, word in enumerate(words):
            wordLen = len(word)
            #or s.startwith(word)
            if s[:wordLen] == word:
                cnt += 1
            
        return cnt
            
    
