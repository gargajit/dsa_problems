class Solution:
    # @param A : list of integers
    # @param B : integer
     # @return an long
    def solve(self, A, B):
        N = len(A)
        s = 0
        
        for i in range(B):
            s += A[i]
        
        max_sum = s

        i = 1
        j = B
        while j < N:
            s += A[j] - A[i-1]
            max_sum = max(max_sum, s)
            i += 1
            j += 1
        
        return max_sum
