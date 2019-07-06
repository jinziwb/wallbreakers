class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        sCounter = collections.Counter(s)
        
        for i,letter in enumerate(s): 
            if sCounter[letter] == 1:
                return i
        return -1
