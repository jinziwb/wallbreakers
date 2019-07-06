class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        candyDict = {}
        for candy in candies: 
            candyDict[candy] = candyDict.get(candy,0) + 1
        print(candyDict)
        
        numCandies = len(candies)/2
        print(numCandies)
        
        values = candyDict.values()
        
        values.sort(reverse = True)
        
        brother = 0
        sister = 0
        types = 0
        valuesIndex = 0
        while sister != numCandies and valuesIndex != len(values):
            if values[valuesIndex] == 1:
                sister += 1
                types += 1
            else: 
                sister += 1
                types += 1
                brother += values[valuesIndex] - 1
            valuesIndex += 1
        return types
