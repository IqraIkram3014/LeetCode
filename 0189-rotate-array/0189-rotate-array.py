class Solution(object):
    def rotate(self, nums, k):
        
        k %= len(nums) # k = 7 % 6 == 1 so k is 1
        nums[:] = nums[-k:] + nums[:-k]

        