## runtime: 90:97%, Memory: 38.56%
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([_s[-1::-1] for _s in s.split()])
    
    
data = ["Let's take LeetCode contest", "God Ding", ]
results = ["s'teL ekat edoCteeL tsetnoc", "doG gniD"]
is_success = True
    
sol = Solution()
for idx, _data in enumerate(data):
    ret = sol.reverseWords(_data)
    if ret != results[idx]:
        is_success = False
        
        print (f"Failed: idx:{idx}")
        print (f"Outputs: {ret}")
        print (f"Expected: {results[idx]}")
        
if is_success:
    print ("Success!!")
