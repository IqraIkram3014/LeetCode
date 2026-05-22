class Solution(object):

    def build(self, text):

        stack = []

        for i in text:

            if i == "#":

                if stack:   # checks emptiness
                    stack.pop()

            else:
                stack.append(i)

        return "".join(stack)

    def backspaceCompare(self, s, t):

        return self.build(s) == self.build(t)