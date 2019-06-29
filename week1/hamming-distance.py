class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        binX = bin(x)[2:]
        binY = bin(y)[2:]
        print(binX, binY)
        
        length = max(len(binX),len(binY))
        print(length)
        
        if len(binX) < length:
            diff = length - len(binX)
            binX = diff * str(0) + binX
            
        if len(binY) < length:
            diff = length - len(binY)
            binY = diff * str(0) + binY
        
        ham = 0
        for i in range(length):
            if binX[i] != binY[i]:
                ham += 1
        return ham
