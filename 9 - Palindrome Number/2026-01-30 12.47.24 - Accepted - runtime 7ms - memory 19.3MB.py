class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # Step 1: Negative numbers are not palindrome
        if x < 0:
            return False
        
        # Step 2: Numbers ending with 0 (except 0 itself) are not palindrome
        if x % 10 == 0 and x != 0:
            return False
        
        # Step 3: Store original number
        original = x
        
        # Step 4: Reverse the number
        reverse = 0
        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10
        
        # Step 5: Compare original and reversed
        return original == reverse
