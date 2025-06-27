class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        max = A[0]

        for i in range(1, N):
            if A[i] > max:
                max = A[i]
        
        total_secs = 0
        for item in A:
            total_secs += max - item
        
        return total_secs


                    
