class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sCount = collections.Counter(s)
        tCount = collections.Counter(t)
        
        for t in tCount:
            if t not in sCount or tCount[t] > sCount[t]:
                return t
