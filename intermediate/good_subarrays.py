'''
Given an array of integers A, a subarray of an array is said to be good if it fulfills any one of the criteria:

1. Length of the subarray is be even, and the sum of all the elements of the subarray must be less than B.

2. Length of the subarray is be odd, and the sum of all the elements of the subarray must be greater than B.

Your task is to find the count of good subarrays in A.
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        subArrLen = 0
        currSum = 0
        cnt = 0

        Ps = [0]*N
        Ps[0] = A[0]

        for i in range(1, N):
            Ps [i] = Ps[i-1] + A[i]
        
        for i in range(N):
            for j in range(i, N):
                subArrLen = j - i + 1
                if i > 0:
                    currSum = Ps[j] - Ps[i-1]
                else:
                    currSum = Ps[j]
                
                if (subArrLen % 2 == 0 and currSum < B) or (subArrLen % 2 != 0 and currSum > B):
                    cnt += 1
                
        return cnt



# if (subArrLen % 2 == 0 and currSum < B) or (subArrLen % 2 != 0 and currSum > B):
