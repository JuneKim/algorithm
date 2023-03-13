## Runtime: 14%, Memory: 40.40%
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
                    li_ret.append(0)
                    continue
                
                li_dry_days.append(idx) ## dry days
                li_ret.append(0)
                
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
                        #print (li_rains_cp)
                        #print (dic_current_lakes)
                        #print (li_ret)
                        #print ("Do not come")
                        return []
                            
                    li_ret[idx_found] = rain
                    li_dry_days.remove(idx_found)
                            
                    li_rains_cp[rain_idx] = -10 ## empty               
                
                dic_current_lakes[str(rain)] = idx
                li_ret.append(-1)
                #print (li_ret)
        li_ret = [1 if i == 0 else i for i in li_ret]
        #print (li_rains_cp)
        #print (dic_current_lakes)
        #print (li_ret)
        return li_ret
