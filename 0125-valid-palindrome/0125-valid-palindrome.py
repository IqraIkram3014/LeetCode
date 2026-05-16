class Solution(object):
    def isPalindrome(self, s):
        """s = ''.join(a.lower() for a in s if a.isalnum())
        return s == s[::-1]"""

        cleared = ""

        for i in s:
            if i.isalnum():
                cleared += i.lower()

        left = 0
        right = len(cleared) - 1

        while left < right:

            if cleared[left] == cleared[right]:
                left += 1
                right -= 1

            else:
                return False

        return True
        
        
            
        
        