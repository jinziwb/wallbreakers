class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if len(g) == 0 or len(s) == 0:
            return 0
        
        g = sorted(g, reverse = True)
        s = sorted(s, reverse = True)
        
        content = 0
        sIndex = 0
        i = 0
        while sIndex < len(s) and i < len(g):
            if s[sIndex] >= g[i]:
                content += 1
                sIndex += 1
                i += 1
            else:
                i += 1
        return content
