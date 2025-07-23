class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        current_sum = 0

        for i in range(B):
            current_sum += A[i]
        
        min_sum = current_sum
        idx = 0
        i = 1
        j = B
        while j < N:
            current_sum += A[j] - A[i-1]

            if current_sum < min_sum:
                min_sum = current_sum
                idx = i
            
            i += 1
            j += 1
        
        return idx



        '''
        N = len(A)
        current_sum = 0
        for i in range(B):
            current_sum += A[i]
        
        idx = i
        i = 1
        j = B
        while j < N:
            if A[j] < A[i-1]:
                current_sum += A[j] - A[i-1]
                idx = i
            i += 1
            j += 1
            
        return idx
        '''
