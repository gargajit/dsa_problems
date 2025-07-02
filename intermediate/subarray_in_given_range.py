class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        res = []
        
        while B <= C:
            res.append(A[B])
            B += 1
        
        return res
