class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ""
        l1,l2 = 0,0
        while l1 < len(word1) and l2 < len(word2):
            if word1[l1:] > word2[l2:]:
                result += word1[l1]
                l1+=1
            else:
                result += word2[l2]
                l2+=1
        result+=word1[l1:]
        result+=word2[l2:]   
        return result
        