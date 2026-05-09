class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """num_idx = {num:index for index, num in enumerate(nums)}   
        for index, num in enumerate(nums):
            sub = target - num
            if sub in num_idx:
                if num_idx[sub]!=index:
                    return[index, num_idx[sub]]
                    break"""

        arr = []
        for index, num in enumerate(nums):
            arr.append((num, index))

        arr.sort() #[(2,0) (7,1) (11,2) (15,3)] this is (2,0) arr[left] and [0] means tuple's index

        left = 0 
        right = len(arr) - 1 # 3

        while left < right:
            curr_sum = arr[left][0] + arr[right][0]

            if curr_sum == target:
                return(arr[left][1], arr[right][1])

            elif curr_sum < target:
                left+=1
            
            else:
                right-=1

        
        
                                                        