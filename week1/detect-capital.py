class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.islower() or word.isupper():
            return True
        if word[0].isupper() and word[1:].islower():
            return True
        else:
            return False
