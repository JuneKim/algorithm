## runtime: 54.53%, memory: 31.97%
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        li_departs = []
        li_dests = []
        for path in paths:
            li_departs.append(path[0])
            if path[0] in li_dests:
                li_dests.remove(path[0])
                
            if path[1] in li_departs:
                li_departs.remove(path[1])
            else:
                li_dests.append(path[1])
        
        #print (li_departs)
        #print (li_dests)
        return li_dests[0]
    
data = [[["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]], [["B","C"],["D","B"],["C","A"]], [["A","Z"]]]
results = ["Sao Paulo" , "A", "Z"]
is_success = True
    
sol = Solution()
for idx, _data in enumerate(data):
    ret = sol.destCity(_data)
    if ret != results[idx]:
        is_success = False
        
        print (f"Failed: idx:{idx}")
        print (f"Outputs: {ret}")
        print (f"Expected: {results[idx]}")
        
if is_success:
    print ("Success!!") 
