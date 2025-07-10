class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def sumOfOddIndexedElements(self, A, B):
        N = len(A)
        Ps = [0] * N
        Q = len(B)
        res = [0] * Q

        # Odd indexed based Prefix Sum 
        for i in range(1, N):
            if i % 2 == 1:
                Ps[i] = Ps[i-1] + A[i]
            else:
                Ps[i] = Ps[i-1]
        
        # 
        for i in range(Q):
            L = B[i][0]
            R = B[i][1]

            if L > 0:
                res[i] = Ps[R] - Ps[L-1]
            else:
                res[i] = Ps[R]
        
        return res
