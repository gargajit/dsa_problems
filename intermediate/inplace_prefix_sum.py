class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        N = len(A)


        for i in range(1, N):
            A[i] = A[i-1] + A[i]
        
        return A
