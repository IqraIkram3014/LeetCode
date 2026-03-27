class Solution(object):
    def findDifference(self, nums1, nums2):
        answer = [[],[]]
        num1set = set(nums1)
        num2set = set(nums2)
        for num in num1set:
            if num not in num2set:
                answer[0].append(num)

        for nums in num2set:
            if nums not in num1set:
                answer[1].append(nums)
        return answer
        