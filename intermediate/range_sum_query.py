class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    def rangeSum(self, A, B):
        N = len(A)
        M = len(B)
        res = []
        Ps = [0] * N
        Ps[0] = A[0]
        
        # Prefix Sum array
        for i in range(1, N):
            Ps[i] = Ps[i-1] + A[i]
        
        for i in range(M):
            L = B[i][0]
            R = B[i][1]

            if L > 0:
                res.append(Ps[R] - Ps[L-1])
            else:
                res.append(Ps[R])
        
        return res
