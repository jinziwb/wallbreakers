class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ""
        shortestStr = strs[0]
        shortestLen = len(shortestStr)
        for eachStr in strs:
            if len(eachStr) < shortestLen:
                shortestStr = eachStr
                shortestLen = len(shortestStr)
        
        longestPref = ""
        i = 0
        for i in range(shortestLen+1):
            pre = shortestStr[:i]
            for eachStr in strs:
                if not eachStr.startswith(pre):
                    return longestPref
            longestPref = pre
        return longestPref
            
