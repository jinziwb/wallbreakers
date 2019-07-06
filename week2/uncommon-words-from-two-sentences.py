class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        aWords = countDict(A)
        bWords = countDict(B)
        
        unique = []
        for word in aWords: 
            if aWords[word] == 1 and word not in bWords: 
                unique.append(word)
        for word in bWords:
            if bWords[word] == 1 and word not in aWords:
                unique.append(word)
        return unique          

def countDict(A):
    aWords = {}
    for word in A.split(" "):
        aWords[word]= aWords.get(word, 0) + 1
    return aWords


