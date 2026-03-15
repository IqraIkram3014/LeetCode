class Solution(object):
    def repeatedSubstringPattern(self, s):
        doubled = s+s
        middle = doubled[1:-1]
        if s in middle:
            return True
        else: 
            return False