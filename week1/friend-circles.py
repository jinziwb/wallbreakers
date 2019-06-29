class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        
        rows = len(M)
        if rows == 0:
            return 0
        cols = len(M[0])
        
        visited = [[0 for i in range(cols)] for j in range(rows)]
        
        def dfs(i,j):
            
            for k in range(cols):
                if visited[i][k] == 0:
                    visited[i][k] = 1
                    if M[i][k] == 1:
                        dfs(i,k)
            for l in range(rows):
                if visited[l][j] == 0:
                    visited[l][j] = 1
                    if M[l][j] == 1:
                        dfs(l,j)
            
        numCircles = 0
        for i in range(rows):
            for j in range(cols):
                if visited[i][j] == 0:
                    visited[i][j] = 1
                    if M[i][j] == 1:
                        numCircles += 1
                        dfs(i,j)
        
        return numCircles 
