## runtime: 17.78%, memory: 49.32%
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num > 0:
            remainder = num
        else:
            remainder = 4294967296 + num
            
        mymap = {10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}
        nums = []
        ## negative??
        while remainder > 0:
            cal = remainder % 16
            if cal > 9:
                nums.append(mymap[cal])
            else:
                nums.append(str(cal))
            remainder = remainder // 16

        return "".join([n for n in nums[::-1]])
    
## runtime: 47.14%, memory: 94.75%
class Solution1:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        mp = "0123456789abcdef"
        ans = ""
        for i in range(8):
            n = num & 15
            c = mp[n]
            ans = c + ans
            num = num >> 4
        return ans.lstrip('0')


data = [26, -1]
results = ["1a", "ffffffff"]
is_success = True
    
sol = Solution()
for idx, _data in enumerate(data):
    ret = sol.toHex(_data)
    if ret != results[idx]:
        is_success = False
        
        print (f"Failed: idx:{idx}")
        print (f"Outputs: {ret}")
        print (f"Expected: {results[idx]}")
        
if is_success:
    print ("Success!!")
