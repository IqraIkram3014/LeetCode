class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num2idx={num:idx for idx, num in enumerate(nums2)}
        ans={}
        for num in nums1:
            j = num2idx[num]
            ans[num]=-1
            for k in range(j+1,len(nums2)):
                if nums2[k]>num:
                    ans[num]=nums2[k]
                    break
        return [ans[num] for num in nums1]
        