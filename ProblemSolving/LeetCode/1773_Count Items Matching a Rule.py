## runtime: 33.31%, memory: 75.72%
class Solution1:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        dic_items = {}
        for idx, val in enumerate(items):
            dic_items[idx] = {"type": val[0], "color": val[1], "name":val[2]}
        
        myCnt = 0
        for key in dic_items.keys():
            if dic_items[key][ruleKey] == ruleValue:
                myCnt +=1
                
        return myCnt

## runtime: 94.44%, memory: 75.72%
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            myId = 0
        elif ruleKey == "color":
            myId = 1
        elif ruleKey == "name":
            myId = 2
        else:
            return 0
               
        myCnt = 0
        for idx, val in enumerate(items):
            if val[myId] == ruleValue:
                myCnt += 1

        return myCnt

    
data = [[[["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver"], [[["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], "type", "phone"]]
results = [1, 2]
is_success = True
    
sol = Solution()
for idx, _data in enumerate(data):
    ret = sol.countMatches(_data[0], _data[1], _data[2])
    if ret != results[idx]:
        is_success = False
        
        print (f"Failed: idx:{idx}")
        print (f"Outputs: {ret}")
        print (f"Expected: {results[idx]}")
        
if is_success:
    print ("Success!!")
