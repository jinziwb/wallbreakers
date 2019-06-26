class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        i = 0
        j = len(s) - 1
        
        while not i > j:
            while not s[i].isalnum() and not i == j:
                i+=1
            while not s[j].isalnum() and not i == j:
                j-=1
            if s[i].lower() != s[j].lower():
                return False
            else:
                i+=1
                j-=1
        return True
