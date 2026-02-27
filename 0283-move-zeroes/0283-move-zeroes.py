class Solution(object):
    def moveZeroes(self, nums):
        add_zero = 0  # pointer for next non-zero position

        # Step 1: non-zero numbers ko left shift karo
        for num in nums:
            if num != 0:
                nums[add_zero] = num
                add_zero += 1

        # Step 2: baaki positions zero se fill karo
        while add_zero < len(nums):
            nums[add_zero] = 0
            add_zero += 1

        return nums