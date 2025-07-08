class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        Ps_odd = [0] * N
        Ps_even = [0] * N

        Ps_odd[0] = 0
        Ps_even[0] = A[0]

        # Odd indexed Prefix Sum
        for i in range(1,N):
            if i % 2 == 1:
                Ps_odd[i] = Ps_odd[i-1] + A[i]
            else:
                Ps_odd[i] = Ps_odd[i-1]

        # Even indexed Prefix Sum  
        for i in range(1, N):
            if i % 2 == 0:
                Ps_even[i] = Ps_even[i-1] + A[i]
            else:
                Ps_even[i] = Ps_even[i-1]

        
        cnt = 0
        if ((Ps_even[N-1] - Ps_even[N-1]) == (Ps_odd[N-1] - Ps_odd[0])):
            cnt += 1

        for i in range(1, N):
            if ((Ps_odd[i-1] + Ps_even[N-1] - Ps_even[i]) == (Ps_even[i-1] + Ps_odd[N-1] - Ps_odd[i])):
                cnt += 1

        return cnt
