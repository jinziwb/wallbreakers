class Solution(object):
    def transpose(self, A):
        transposeA = []
        for i in range(len(A[0])):
            transposeRow = []
            for j in range(len(A)):
                transposeRow.append(A[j][i])
            transposeA.append(transposeRow)
        return transposeA
