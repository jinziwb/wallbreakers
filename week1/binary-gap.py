class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        binary = bin(N)[2:]

        currentIndex = binary.find(str(1))
        nextIndex = 0   
        maxDist = 0
        
        while (nextIndex != -1): 
            nextIndex = binary.find(str(1),currentIndex+1)
            maxDist = max(maxDist, nextIndex-currentIndex)
            currentIndex = nextIndex 
        return maxDist
            
