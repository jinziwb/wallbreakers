class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        sCount = collections.Counter(s)
        
        printStr = ""
        for key in sCount.most_common():
            printStr += key[1] * key[0] 
            
        return printStr
