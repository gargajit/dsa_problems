'''
iven an array of integers A and an integer B, find and return the minimum number of swaps required to bring all the numbers less than or equal to B together.

Note: It is possible to swap any two elements, not necessarily consecutive.
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        count_good = 0

        for i in range(N):
            if A[i] <= B:
                count_good += 1

        bad = 0

        for i in range(0, count_good):
            if A[i] > B:
                bad += 1
        
        minSwaps = bad

        for i in range(1, N - count_good + 1):
            if A[i - 1] > B:
                    bad -= 1
            
            if A[i + count_good - 1] > B:
                bad += 1
                
            minSwaps = min(minSwaps, bad)

        return minSwaps
 
