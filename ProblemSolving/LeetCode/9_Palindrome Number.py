class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        strX = str(x)
        lenStr = len(strX)
        for idx in range (0, int (lenStr/2)):
            if strX[idx] != strX[lenStr - idx -1]:
                return False
            
        return True
