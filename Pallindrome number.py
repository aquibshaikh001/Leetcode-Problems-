#------------------------------------Code made by me for practice 

# a = 4567
# reversed_num = 0
# while a > 0:
#     digit = a % 10
#     reversed_num = reversed_num * 10 + digit 
#     a = a // 10
# if reversed_num == a :
#     return True
# else :
#     return False

#-------------------------------------------------------------------------

#Final solution


class Solution:
    def isPalindrome(self,x):
    # Negative numbers are not palindromes due to the minus sign
        if x < 0:
            return False
        
        original_num = x
        reversed_num = 0
    
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit 
            x = x // 10
        
        return reversed_num == original_num

        
        
