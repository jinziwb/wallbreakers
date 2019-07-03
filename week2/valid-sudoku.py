class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = 9
        cols = 9 
        
        # check rows
        
        for row in board: 
            numDict = {}
            for num in row: 
                numDict[num] = numDict.get(num, 0) + 1
            for key in numDict.keys():
                if key != '.' and numDict[key] > 1:
                    return False

        # check cols
        for i in range(cols):
            numDict = {}
            for j in range(rows):
                numDict[board[j][i]] = numDict.get(board[j][i], 0) + 1
            for key in numDict.keys():
                if key != '.' and numDict[key] > 1:
                    return False

        # check grid: 
        for i in range(3):
            for j in range(3):
                numDict = {}
                for k in range(3):
                    for l in range(3):
                        numDict[board[3*i + k][3*j + l]] = numDict.get(board[3*i + k][3*j + l], 0) + 1
                for key in numDict.keys():
                    if key != '.' and numDict[key] > 1:
                        return False 
        return True
