## Runtime 39 ms, Beats 87.94%
## Memory 13.9 MB, Beats 70.2%

## 1st solucation
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        if num == "":
            return ""
        li_ret = []
        prev = num[0]
        cnt = 1
        for mynum in num[1:]:
            if mynum == prev:
                cnt += 1
                if cnt == 3:
                    li_ret.append(int(f"{mynum}{mynum}{mynum}"))
                    # add
            else:
                prev = mynum
                cnt = 1
            
        #select max
        if len(li_ret) > 0:
            mymax = max(li_ret)
            if mymax == 0:
                return "000"
            return str(mymax)
        else:
            return ""

## 2nd minor revision
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        if num == "":
            return ""
        li_ret = []
        prev = num[0]
        cnt = 1
        for mynum in num[1:]:
            if mynum == prev:
                cnt += 1
                if cnt == 3:
                    li_ret.append(int(mynum))
            else:
                prev = mynum
                cnt = 1
            
        #select max
        if len(li_ret) > 0:
            mymax = max(li_ret)
            return str(mymax)*3
        else:
            return ""
