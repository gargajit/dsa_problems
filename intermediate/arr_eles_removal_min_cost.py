# Given an integer array A of size N. 
# You can remove any element from the array in one operation.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        A.sort()
        k = 1
        ans = 0

        for i in range(N-1, -1, -1):
            ans += A[i] * k
            k += 1
        
        return ans

