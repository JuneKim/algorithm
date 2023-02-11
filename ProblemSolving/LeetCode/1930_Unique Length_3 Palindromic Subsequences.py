class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Timeout
        #if len(s) == 0:
        #    return 0
        #retCnt = 0
        #resultSubsetList = []
        #totalLen = len(s)

        #def createSubset(tmpStr, currIdx, totalCnt):
        #    if (totalCnt > 3):
        #        return

        #    if totalCnt == 3:
        #        if not tmpStr in resultSubsetList:
        #            if tmpStr[0] == tmpStr[2]:
        #                resultSubsetList.append(tmpStr)
        #        return

        #    if currIdx == totalLen:
        #        return

        #    if totalCnt < 3:
        #        createSubset(tmpStr + s[currIdx], currIdx + 1, totalCnt + 1)
        #        createSubset(tmpStr, currIdx + 1, totalCnt)

        #createSubset("", 0, 0)

        #return len(resultSubsetList)
        cnt = 0
        myKey = set()
        myResult = set()
        for chr in s:
            if not chr in myKey:
                myKey.add(chr)
                i, j = s.find(chr), s.rfind(chr)
                if i > -1:
                    for idx in range(i+1, j):
                        myResult.add(chr + s[idx] + chr)
            
        return len(myResult)
