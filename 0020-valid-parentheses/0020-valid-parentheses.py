class Solution(object):

    def isValid(self, s):

        self.stack = []

        mapping = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for ch in s:

            # closing bracket
            if ch in mapping:

                if self.stack and self.stack[-1] == mapping[ch]:

                    self.stack.pop()

                else:
                    return False

            # opening bracket
            else:
                self.stack.append(ch)

        return True if not self.stack else False