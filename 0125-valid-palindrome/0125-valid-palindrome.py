class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(a.lower() for a in s if a.isalnum())
        return s == s[::-1]
        