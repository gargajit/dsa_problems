class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def maxSubarray(self, A, B, C):

        s = 0
        max_sum = 0

        i = 0
        j = 0
        for j in range(A):
            s += C[j]
            while s > B:
                s -= C[i]
                i += 1
            
            if s > max_sum:
                max_sum = s
        
        return max_sum 
