## runtime: 73.48%, memory: 51.80%
class Solution:
    def convertToBase7(self, num: int) -> str:
        li_ret = []
        target = num
        if target == 0:
            return "0"


        if target < 0:
            target = -target
            
        base = 7

        while target >= base:
            quotinent = target // base
            remainder = target % base
            li_ret.append(remainder)
            target = quotinent
        
        if target != 0:
            li_ret.append(target)

        str_ret = "".join(list(map(str, li_ret[-1::-1])))
        if num < 0:
            str_ret = "-" + str_ret

        return str_ret
