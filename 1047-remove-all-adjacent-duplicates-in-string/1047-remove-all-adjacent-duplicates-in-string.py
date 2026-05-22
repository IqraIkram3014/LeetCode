class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.stack=[]
        for ch in s:
            if self.stack and self.stack[-1] == ch:
                self.stack.pop()
            else:
                self.stack.append(ch)
        return "".join(self.stack)