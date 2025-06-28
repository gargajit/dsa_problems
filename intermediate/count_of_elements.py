class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        cnt = 0

        max_val = max(A)

        for item in A:
            if item < max_val:
                cnt += 1
        
        return cnt
