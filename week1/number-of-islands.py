class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        
        visited = [[0 for i in range(cols)] for j in range(rows)]
        
        numIslands = 0
        
        def dfs(iVar,jVar):
            offsets = [[-1,0],[0,-1],[1,0],[0,1]]

            for offset in offsets: 
                iNew = iVar + offset[0]
                jNew = jVar + offset[1]

                if iNew >= 0 and iNew < rows and jNew >= 0 and jNew < cols and visited[iNew][jNew] == 0: 
                    visited[iNew][jNew] = 1
                    if grid[iNew][jNew] == "1":
                        dfs(iNew,jNew)
                        
        for i in range(rows):
            for j in range(cols):
                if visited[i][j] == 0:
                    visited[i][j] = 1
                    if grid[i][j] == "1": 
                        numIslands += 1
                        dfs(i,j)

        return numIslands

