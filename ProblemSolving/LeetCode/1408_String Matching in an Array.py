class Solution1:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key = len)
        li_ret = []
        for idx, val in enumerate(words[:-1:1]):
            valLen = len(val)
            for target in words[idx+1:]:
                targetLen = len(target)
                for idy in range(targetLen-valLen+1):
                    if val == target[idy:idy+valLen] and val not in li_ret:
                        li_ret.append(val)
                        break
        return li_ret
    
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        target = " ".join(words)
        return [word for word in words if target.count(word) > 1]
    
data = [["mass","as","hero","superhero"], ["leetcode","et","code"], ["blue","green","bu"], ["leetcoder","leetcode","od","hamlet","am"]]
result = [["as","hero"], ["et","code"], [], ["od","am","leetcode"]]
sol = Solution()
is_success = True
for _idx, _data in enumerate(data):
    ret = sol.stringMatching(_data)
    if result[_idx] != ret:
        print (f"Failed. {_idx}")
        print (f"Output:{ret}")
        print (f"Expected:{result[_idx]}")        
        is_success = False
        
if is_success:
    print ("Success!!")
