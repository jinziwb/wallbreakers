class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        unique = set()
        for word in words:
            transformation = ""
            for letter in word:
                transformation = transformation + morse[ord(letter)-96-1]
            unique.add(transformation)
        return len(unique)
