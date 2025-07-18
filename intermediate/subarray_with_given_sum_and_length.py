class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        N = len(A)

        s = 0
        for i in range(B):
            s += A[i]
        
        if s == C:
            return 1

        i = 1
        j = B
        while j < N:
            s += A[j] - A[i-1]

            if s == C:
                return 1
            i += 1
            j += 1
        
        return 0
