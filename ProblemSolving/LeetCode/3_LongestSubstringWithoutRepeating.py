from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp_result = list()
        max_cnt = 0
        for ch in s:
            if ch in tmp_result:
                if len(tmp_result) > max_cnt:
                    max_cnt = len(tmp_result)
                    
                idx = tmp_result.index(ch)
                tmp_result = tmp_result[idx+1:]
            
            tmp_result.append(ch)
                
        if len(tmp_result) > max_cnt:
            max_cnt = len(tmp_result)
            
        return max_cnt
'''     
        max_cnt = 0
        sam_cnt = dict()
        cur_cnt = 0
        for ch in s:
            if ch in sam_cnt.keys():
                if cur_cnt > max_cnt:
                    max_cnt = cur_cnt
                    
                tmp_cnt = sam_cnt[ch]
                del_list = []
                for tmp in sam_cnt.keys():
                    if sam_cnt[tmp] > tmp_cnt:
                        sam_cnt[tmp] -= tmp_cnt
                    else:
                        del_list.append(tmp)
                        
                for da_del in del_list:
                    del sam_cnt[da_del]
                cur_cnt = cur_cnt - tmp_cnt              
            cur_cnt += 1
            sam_cnt[ch]  = cur_cnt

        if cur_cnt > max_cnt:
            return cur_cnt
        
        return max_cnt
'''
