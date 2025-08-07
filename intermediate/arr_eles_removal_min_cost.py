# Given an integer array A of size N. 
# You can remove any element from the array in one operation.

class Solution:
    def solve(self, A):
        N = len(A)
        A.sort()        // sort the array
        k = 1
        ans = 0           // stores answer

        for i in range(N-1, -1, -1):        // removing bigger value first to reduce cost
            ans += A[i] * k
            k += 1
            
        return ans
