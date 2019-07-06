class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        pCounter = collections.Counter(p)
        
        indices = []
        for i in range(len(s)-len(p)+1):
            if s[i] in p:
                sub = s[i:i+len(p)]
                if collections.Counter(sub) == pCounter:
                    indices.append(i)
        return indices
