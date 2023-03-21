## runtime: 64%, memory: 44.22%
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        dict_myMap = {"a": 0, "b": 1, "c": 2, "d":3, "e":4, "f":5, "g":6, "h":7}
        myCnt = dict_myMap[coordinates[0]] + int(coordinates[1])
        return True if myCnt % 2 == 0 else False
    
data = ["a1", "h3", "c7"]
result = [False, True, False]
sol = Solution()
is_success = True
for _idx, _data in enumerate(data):
    ret = sol.squareIsWhite(_data)
    if result[_idx] != ret:
        print (f"Failed. {_idx}")
        print (f"Output:{ret}")
        print (f"Expected:{result[_idx]}")        
        is_success = False
        
if is_success:
    print ("Success!!")
