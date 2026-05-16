class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleared = ""

        for i in s:
            if i.isalnum():
                cleared += i.lower()

        def check(left, right):

            while left < right:

                if cleared[left] != cleared[right]:
                    return False

                left += 1
                right -= 1

            return True

        left = 0
        right = len(cleared) - 1

        while left < right:

            if cleared[left] == cleared[right]:
                left += 1
                right -= 1

            else:
                return (
                    check(left + 1, right)
                    or
                    check(left, right - 1)
                )

        return True
        