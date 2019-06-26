class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        wordList = s.split(" ")
        print(wordList)
        revS = ""
        for word in wordList:
            revS += word[::-1]
            revS += " "
        return revS.strip()

