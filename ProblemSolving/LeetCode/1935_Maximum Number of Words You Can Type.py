# runtime: 93.91%, memory: 56.52%
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        li_txt = text.split(" ")
        myCnt = 0
        for txt in li_txt:
            is_found = False
            for broken in brokenLetters:
                if broken in txt:
                    is_found = True
                    break
            if not is_found:
                myCnt += 1

        return myCnt
        
        
data = [[ "hello world", "ad"], ["leet code", "lt"], [ "leet code", "e"]]
result = [1,1,0]
sol = Solution()
is_success = True
for _idx, _data in enumerate(data):
    ret = sol.canBeTypedWords(_data[0], _data[1])
    if result[_idx] != ret:
        print (f"Failed. {_idx}")
        print (f"Output:{ret}")
        print (f"Expected:{result[_idx]}")        
        is_success = False
        
if is_success:
    print ("Success!!")
