class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber == 0:
            return ""
        myUnit = 26
        target = columnNumber
        result = ""
        ## XYX == X * 26*2 + Y*26 + Z
        while target > 0:
            target -= 1
            result = chr(target % myUnit + 65) + result
            target //= myUnit
            
        return result
    
data = [1, 28, 701, 52, 27]
result = ["A", "AB", "ZY", "AZ", "AA"]
sol = Solution()
is_success = True
for _idx, _data in enumerate(data):
    ret = sol.convertToTitle(_data)
    if result[_idx] != ret:
        print (f"Failed. {_idx}")
        print (f"Output:{ret}")
        print (f"Expected:{result[_idx]}")        
        is_success = False
        
if is_success:
    print ("Success!!")
