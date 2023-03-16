## runtime: 15.87%, memory: 44.54%
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        def countWord(s: str):
            myList = {}
            for ch in s:
                if ch in myList.keys():
                    myList[ch] += 1
                else:
                    myList[ch] = 1
            return myList
            
        ransomDic = countWord(ransomNote)
        magDic = countWord(magazine)
        
        for key, val in ransomDic.items():
            if not key in magDic.keys() or magDic[key] < val:
                print (ransomDic)
                print (magDic)
                print ("Error")
                return False
            
        return True
      
## runtime: 84.12%, memory: 44.54%
class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {i:magazine.count(i) for i in set(magazine)}
        ran = {i:ransomNote.count(i) for i in set(ransomNote)}
        
        for i in ran.keys():
            if not i in mag.keys():
                return False
            elif mag[i] < ran[i]:
                return False
            
        return True
                
    
    
data = [["a", "b"], ["aa", "ab"], ["aa", "aab"], ["fffbfg", "effjfggbffjdgbjjhhdegh"] ]
results = [False, False, True , True]
is_success = True
    
sol = Solution()
for idx, _data in enumerate(data):
    ret = sol.canConstruct(_data[0], _data[1])
    if ret != results[idx]:
        is_success = False
        
        
 
        
        print (f"Failed: idx:{idx}")
        print (f"Outputs: {ret}")
        print (f"Expected: {results[idx]}")
        
if is_success:
    print ("Success!!")
