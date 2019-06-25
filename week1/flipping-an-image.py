class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        revA = []
        for i in range(len(A)):
            rev = []
            for j in range(len(A[0])-1, -1, -1):
                rev.append(1-A[i][j])
            revA.append(rev)
        return revA
