class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiou"
        i = 0
        j = len(s) - 1
        
        while i < j:
            while s[i] not in vowels and i < j:
                i+=1
            while s[j] not in vowels and i < j and j >= 0:
                j-=1
            i+=1
            j+=1
        print(s)
