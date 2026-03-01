class Solution(object):
    def mergeAlternately(self, word1, word2):
        
        result = ""
        for i in range(min(len(word1),len(word2))):
            result += word1[i]
            result += word2[i]

        result += word1[i+1:]
        result += word2[i+1:]

        return result
        