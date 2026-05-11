class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i=0
        j=1
        result = [0] * len(nums)
        for num in nums:
            if num % 2 == 0:
                result[i] = num
                i+=2
                
            else:
                result[j] = num
                j+=2
        return result
        