## runtime: 75.65%, memory: 20.41% 
class Solution1:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        b_outcome = 0x00
        volume = length * width * height
        
        if length >= 10**4 or width >= 10**4 or height >= 10**4 or volume >= 10**9:
            b_outcome |= 0x1
        
        if mass >= 100:
            b_outcome |= 0x10
        
        if b_outcome == 0x11:
            return "Both"
        elif b_outcome == 0x1:
            return "Bulky"
        elif b_outcome == 0x10:
            return "Heavy"
        
        return "Neither"
    
## runtime: 46%, memory: 20.41% 
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        idx = 0x00
        volume = length * width * height
        
        if length >= 10**4 or width >= 10**4 or height >= 10**4 or volume >= 10**9:
            idx |= 0x1
        
        if mass >= 100:
            idx |= 0x2
         
        return ("Neither", "Bulky", "Heavy", "Both")[idx]
    
    
data = [[1000, 35, 700, 300], [ 200, 50, 800, 50]]
result = ["Heavy", "Neither"]
sol = Solution()
is_success = True
for _idx, _data in enumerate(data):
    ret = sol.categorizeBox(_data[0], _data[1], _data[2], _data[3])
    if result[_idx] != ret:
        print (f"Failed. {_idx}")
        print (f"Output:{ret}")
        print (f"Expected:{result[_idx]}")        
        is_success = False
        
if is_success:
    print ("Success!!")
