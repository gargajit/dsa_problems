class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        min_val = min(A)
        max_val = max(A)

        if min_val == max_val:
            return 1
        
        last_min_index = -1
        last_max_index = -1
        min_length = N

        for i in range(N):
            if A[i] == min_val:
                last_min_index = i
                if last_max_index != -1:
                    min_length = min(min_length, i - last_max_index + 1)        
                
            if A[i] == max_val:
                last_max_index = i
                if last_min_index != -1:
                    min_length = min(min_length, i - last_min_index + 1)
                       
        return min_length
