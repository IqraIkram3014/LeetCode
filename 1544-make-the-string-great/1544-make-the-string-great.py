class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.stack=[]

        for ch in s:
            if self.stack and abs(ord(self.stack[-1])-ord(ch))==32: #abs give positive int means -32 to 32 and ord gives ASCII values of letters and self.stack check emptiness
                self.stack.pop()
            else:
                self.stack.append(ch)
        
        return "".join(self.stack)


            
            


