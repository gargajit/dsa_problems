class Solution:
    # @param A : list of integers
     # @return an long
    def subarraySum(self, A):
        N = len(A)
        total = 0

        for i in range(N):
            total += A[i] * (i+1) * (N-i)
        
        return total
