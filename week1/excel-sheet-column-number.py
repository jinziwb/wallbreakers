class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i in range(len(s)):
            power = 26 ** (len(s) - 1 - i)
            total += power * (ord(s[i]) - 64)
        return total
