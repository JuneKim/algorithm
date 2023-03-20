from collections import Counter
## runtime: 61.97%, memory: 79.69%
class Solution:
    def countMatches(self, words1: List[str], words2: List[str]) -> int:
        
        if len(words1) == 0 or len(words2) == 0:
            return 0
        
        dict_words1 = Counter(words1)
        dict_words2 = Counter(words2)
        
        myCnt = 0
        for key in dict_words1.keys(): 
            if dict_words1[key] == 1:
                if key in dict_words2.keys() and dict_words2[key] == 1:
                    myCnt += 1

        return myCnt
        
        
data = [[["leetcode","is","amazing","as","is"], ["amazing","leetcode","is"]], [["b","bb","bbb"], ["a","aa","aaa"]], [["a","ab"],  ["a","a","a","ab"]]]
results = [2, 0, 1]
is_success = True
    
sol = Solution()
for idx, _data in enumerate(data):
    ret = sol.countMatches(_data[0], _data[1])
    if ret != results[idx]:
        is_success = False
        
        print (f"Failed: idx:{idx}")
        print (f"Outputs: {ret}")
        print (f"Expected: {results[idx]}")
        
if is_success:
    print ("Success!!")
