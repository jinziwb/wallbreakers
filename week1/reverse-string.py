class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        tempChar = ""
        for i in range(len(s)/2):
            index = len(s) - 1 - i
            tempChar = s[index]
            s[index] = s[i]
            s[i] = tempChar
        return s
