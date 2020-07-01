class Solution:
    def reverse(self, x: int) -> int:
        ret_str = list()
        is_pos = 0
  
        tmp_str = str(x)
        is_start = 0
        for ch in tmp_str[::-1]:
            if is_start or ch is not '0':
                ret_str.append(ch)
                is_start = 1

        if len(ret_str) == 0 or x > 2147483647 or x < -2147483648 :
            return 0
                
        if ret_str[-1] == '-':
            ret_int = int("".join(ret_str[0:-1]))
            ret_int = -ret_int
        else:
            ret_int = int("".join(ret_str))
            
        if ret_int > 2147483647 or ret_int < -2147483648:
            return 0
        
        return ret_int
