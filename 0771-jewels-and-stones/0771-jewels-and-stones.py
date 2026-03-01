class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count = 0
        set_jewel = set(jewels)
        
        for stone in stones:
            if stone in set_jewel:
                count += 1
                
        return count