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

    
#n=int(input("Enter number:"))
#temp=n
#rev=0
# reverse a number e.g., 129 -> 921
#while(n>0):
#    dig=n%10
#    rev=rev*10+dig
#    n=n//10
#if(temp==rev):
#    print("The number is a palindrome!")
#else:
#    print("The number isn't a palindrome!")
