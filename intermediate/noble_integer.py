# Given an integer array A, 
#find if an integer p exists in the array such that the number of integers greater than p in the array equals p.

class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
        N = len(A)
        A.sort()
        cnt = 0

        for i in range(N):
            cnt = N - (i + 1)
            if i == N-1 and cnt == A[i]:
                return 1

            elif cnt == A[i] and A[i+1] != A[i]:
                return 1
        
        return -1

