class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        tDict = countLetters(t)
        sDict = countLetters(s)
        
        return tDict == sDict
        
def countLetters(t):
    tDict = {}
    for let in t:
            if let in tDict.keys():
                tDict[let] += 1
            else:
                tDict[let] = 1
    return tDict 
