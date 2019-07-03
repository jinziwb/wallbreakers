class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) != len(str.split(" ")):
            return False
        
        patternDict = {}
        for i,let in enumerate(pattern):
            if let in patternDict:
                patternDict[let].append(i)
            else:
                patternDict[let] = [i]
        
        strsDict = {}
        strs = str.split(" ")
        for i,string in enumerate(strs):
            if string in strsDict:
                strsDict[string].append(i)
            else:
                strsDict[string] = [i]
        
        for i in range(len(pattern)):
            if patternDict[pattern[i]] != strsDict[strs[i]]:
                return False
        return True
