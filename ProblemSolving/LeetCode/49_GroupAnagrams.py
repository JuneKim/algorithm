from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list = []
        ret_list = dict()
        for sample in strs:
            _sorted = str(sorted(sample))
            if len(sorted_list) > 0 and _sorted in sorted_list:
                    ret_list[_sorted].append(sample)
            else:
                sorted_list.append(_sorted)
                ret_list[_sorted] = [sample]
                  
        return [value for value in ret_list.values()]
