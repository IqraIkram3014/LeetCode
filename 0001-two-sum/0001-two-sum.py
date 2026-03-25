class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_idx = {num : index for index, num in enumerate(nums)}
        # {2: 0, 7: 1, 11: 2, 15: 3}
        for index, num in enumerate(nums):
            sub= target-num
            if sub in num_idx:
                if num_idx[sub] != index:
                    return [index, num_idx[sub]]
                    break          
        
        