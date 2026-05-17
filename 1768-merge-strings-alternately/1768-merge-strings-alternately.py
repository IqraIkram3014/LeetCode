class Solution(object):
    def mergeAlternately(self, word1, word2):
        
        result = ""
        l1,l2 = 0,0
        while l1 < len(word1) or l2 < len(word2):
            if l1 < len(word1) and l2 < len(word2):
                result += word1[l1]
                result += word2[l2]
                l1+=1
                l2+=1
            elif l1 < len(word1) and l2 >= len(word2):
                result += word1[l1]
                l1+=1
            else:
                result += word2[l2]
                l2+=1
        return result


        

        
        