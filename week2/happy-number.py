class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n not in seen:
            seen.add(n)
            happySum = 0
            while n > 0:
                digit = n % 10
                happySum += digit ** 2
                n = n/10
            n = happySum
        if 1 in seen:
            return True
        else:
            return False

