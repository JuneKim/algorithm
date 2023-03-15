# runtime: 63.15%, memory: 55.6%
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        moves = {"N": [0, 1], "S": [0, -1], "E": [1,0], "W": [-1,0]}
        positions = [[0,0]]
        current = [0, 0]
        for s in path:
            current = [current[0] + moves[s][0], current[1] + moves[s][1]]
            if current in positions:
                return True
            positions.append(current)

        return False
    
    
data = ["NES", "NESWW", ]
results = [False, True]
is_success = True
    
sol = Solution()
for idx, _data in enumerate(data):
    ret = sol.isPathCrossing(_data)
    if ret != results[idx]:
        is_success = False
        
        print (f"Failed: idx:{idx}")
        print (f"Outputs: {ret}")
        print (f"Expected: {results[idx]}")
        
if is_success:
    print ("Success!!")
