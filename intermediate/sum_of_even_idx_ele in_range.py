class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def sumOfEvenIndexedElements(self, A, B):
        N = len(A)
        Q = len(B)
        res = []

        Ps = [0] * N
        Ps[0] = A[0]

        # PrefixSum array for even indexed elements
        for i in range(1, N):
            if i % 2 == 0:
                Ps[i] = Ps[i-1] + A[i]
            else:
                Ps[i] = Ps[i-1]
        
        for i in range(Q):
            L = B[i][0]
            R = B[i][1]

            if L > 0:
                res.append(Ps[R] - Ps[L-1])
            else:
                res.append(Ps[R])
        
        return res
