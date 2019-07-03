class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sDict = getLetterDict(s)
        tDict = getLetterDict(t)
        
        for i in range(len(s)):
            if sDict[s[i]] != tDict[t[i]]:
                return False
        return True
        
def getLetterDict(s):
    letterdict = {}
    for i,letter in enumerate(s): 
        if letter in letterdict:
            letterdict[letter].append(i)
        else:
            letterdict[letter] = [i]
    return letterdict
