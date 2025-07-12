class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        ps = [0]*N
        ps[0] = A[0]

        for i in range(1, N):
            ps[i] = ps[i-1] + A[i]
        
        max_val = ps[B-1]     # prefix
        if B < N:
            max_val = max(max_val, ps[N-1] - ps[N-B-1])   # suffix
        
        for i in range(1, B):
            max_val= max(max_val, ps[i-1] + ps[N-1] - ps[N-(B-i)-1])
        
        return max_val
