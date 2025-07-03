class Solution:
    # @param A : string
     # @return an long
    def solve(self, A):
        count_a = 0
        ans = 0
        n = len(A)
        for i in range(n):
            if A[i] == 'A':
                count_a += 1
            elif A[i] == 'G':
                ans += count_a
        
        return ans
