class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        cnt = 0
        l = 0
        r = 0
        sum = 0

        while r < N:
            sum += A[r]
            while sum >= B and l < r:
                sum -= A[l]
                l += 1
            if sum < B:
                cnt += r - l + 1
            
            r += 1
        
        return cnt
        
        

        
        '''
        max_val = float('-inf')
        N = len(A)
        cnt = 0
        sum = 0

        for i in range(N):
            sum += A[i] * (i+1) * (N-i)
            if sum < B:
                cnt += 1
        
        return cnt
        '''
