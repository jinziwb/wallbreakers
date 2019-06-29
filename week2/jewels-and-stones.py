class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        dictS = {}
        for s in S:
          dictS[s] = dictS.get(s, 0) + 1
        
        numJewels = 0
        for j in J: 
            if j in dictS:
                numJewels += dictS.get(j)
        return numJewels
        
