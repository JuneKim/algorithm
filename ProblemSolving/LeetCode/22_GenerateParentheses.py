from typing import List

class Solution:
    def printAparenthesis (self, n) -> List[str]:
        stack, result = [], []
        def thesis(open, close):
            if open == close == n:
                result.append("".join(stack))

            if open < n:
                stack.append('(')
                thesis(open+1, close)
                stack.pop()

            if open > close:
                stack.append(')')
                thesis(open, close+1)
                stack.pop()

        
        thesis(0,0)
        return result


sol = Solution()
print(sol.printAparenthesis(4))

```
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # memorization
        myDic = {}
        def retList(n: int):
            if n is 0:
                return []
        
            if n is 1:
                return ['()']
            
            if str(n) in myDic.keys():
                return myDic[str(n)]
        
            mySet = set()
                        
            for idx in range(1, n):
                lftList = retList(idx)
                rgtList = retList(n - idx)
                for lft in lftList:
                    for rgt in rgtList:
                        mySet.add(lft+rgt)
            
            mySub = retList (n - 1)
            for sub in mySub:
                mySet.add("(" + sub + ")")
        
            myDic[str(n)] = list(mySet)
            return list(mySet)
        return retList(n)
  ```
