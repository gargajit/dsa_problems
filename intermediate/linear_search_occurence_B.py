    class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        cnt = 0
        for item in A:
            if item == B:
                cnt += 1
        
        return cnt
