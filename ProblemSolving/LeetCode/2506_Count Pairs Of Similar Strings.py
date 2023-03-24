## runtime: 68.94%, memory: 33.50%
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        li_wordCount = [Counter(word) for word in words]
        dict_similartiy = {}
        for dict_wordCount in li_wordCount:
            li_wordKey = list(dict_wordCount.keys())
            li_wordKey.sort()
            wordKey = "".join(li_wordKey)
            if wordKey in dict_similartiy.keys():
                dict_similartiy[wordKey] += 1
            else:
                dict_similartiy[wordKey] = 1

        myCnt = 0
        for val in dict_similartiy.values():
            if val > 1:
                fact = 0
                for i in range(1, val):
                    fact = fact + i
                myCnt += fact
        
        return myCnt
