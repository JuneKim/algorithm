## Runtime: 19.2%, Memory: 37.60%
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        len_rains = len(rains)
        
        li_ret = []
        li_dry_days = [] # idx of drydays
        dic_current_lakes = {} ## id of lake:idx 
        li_rains_cp = rains.copy()
        
        if len_rains == 0:
            return []
        
        for idx, rain in enumerate(rains):
            if rain == 0:
                if idx == 0: # exception
                    li_ret.append(1)
                    continue
                
                li_dry_days.append(idx) ## dry days
                li_ret.append(1)
                
            else:
                if str(rain) in dic_current_lakes.keys():
                    ## search a dry day
                    rain_idx = dic_current_lakes[str(rain)]
                    idx_found = -999
                    for myidx, dry_idx in enumerate(li_dry_days):
                        if dry_idx > rain_idx:
                            idx_found = dry_idx
                            break    
                                
                    if idx_found < 0:
                        return []
                            
                    li_ret[idx_found] = rain
                    li_dry_days.remove(idx_found)
                            
                    li_rains_cp[rain_idx] = -10 ## empty               
                
                dic_current_lakes[str(rain)] = idx
                li_ret.append(-1)
        return li_ret
    
    
## runtime: 55.6%, Memory: 57.6%
#class Solution(object):
#    def avoidFlood(self, rains):
#        """
#        :type rains: List[int]
#        :rtype: List[int]
#        """
#        q=[] # list for zeros positions
#        ans=[]
#        hashmap={}
#        for i in range(len(rains)):
#            if rains[i] == 0:
#                q.append(i)
#                ans.append(1)  # as per example 4
#            else:
#                if rains[i] in hashmap:    
#                    if len(q) == 0:
#                        ans=[]
#                        break
#                    else:
#                        index = hashmap[rains[i]]
#                        # find a zero position just greater than previous occurrence of rains[i]
#                        pos=bisect.bisect_right(q, index) 
#                        if pos<len(q): # no zero exists in between occurrence
#                            ans[q[pos]]=rains[i]
#                            q.pop(pos)
#                        else:
#                            ans=[]
#                            break
#                hashmap[rains[i]]=i
#                ans.append(-1)  
#            
#        return ans
