class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        Ps = [0] * N
        Ps[0] = A[0]

        for i in range(1, N):
            Ps[i] = Ps[i-1] + A[i]

        for i in range(N):
            if i == 0:
                L_sum = 0
                R_sum = Ps[N-1] - Ps[0]
            elif i == N-1:
                L_sum = Ps[i-1]
                R_sum = 0 
            else:
                L_sum = Ps[i-1]
                R_sum = Ps[N-1] - Ps[i]

            if L_sum == R_sum:
                return i
            
        return -1
