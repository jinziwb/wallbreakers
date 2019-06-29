class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        if rows == 0:
            return 0
        cols = len(board[0])
        
        visited = [[0 for j in range(cols)] for k in range(rows)]
        notSurrounded = [[0 for j in range(cols)] for k in range(rows)]
        
        def dfs(i,j):
            offsets = [[-1,0],[1,0],[0,-1],[0,1]]
            
            for offset in offsets: 
                newI = i + offset[0]
                newJ = j + offset[1]
                
                if newI >= 0 and newI < rows and newJ >= 0 and newJ < cols and visited[newI][newJ] == 0:       
                    visited[newI][newJ] = 1
                    if board[newI][newJ] == 'O':
                        notSurrounded[newI][newJ] = 1
                        dfs(newI,newJ)
                        
        
        # top row and bottom row: 
        for j in range(cols):
            if visited[0][j] == 0:
                visited[0][j] = 1
                if board[0][j] == 'O':
                    dfs(0, j)
            if visited[rows-1][j] == 0:
                visited[rows-1][j] = 1
                if board[rows-1][j] == 'O':
                    dfs(rows-1, j)
        # left col and right col:
        for i in range(rows):
            if visited[i][0] == 0:
                visited[i][0] = 1
                if board[i][0] == 'O':
                    dfs(i, 0)
            if visited[i][cols-1] == 0:
                visited[i][cols-1] = 1
                if board[i][cols-1] == 'O':
                    dfs(i, cols-1)
        
        for i in range(1,rows-1):
            for j in range(1,cols-1):
                if board[i][j] == 'O' and notSurrounded[i][j] == 0:
                    board[i][j] = 'X'
