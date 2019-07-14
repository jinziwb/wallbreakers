class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sInd = 0
        tInd = 0
        # compiled = ""
        while sInd < len(s) and tInd < len(t):
            if s[sInd] == t[tInd]:
                # compiled = compiled + t[tInd]
                sInd += 1
                tInd += 1
            else:
                tInd += 1
        return sInd == len(s)
        
                
            
            
            
