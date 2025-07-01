class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def solve(self, A):
        arr = []
        n = len(A)

        for i in range(n):
            for j in range(i, n):
                temp = A[i: j+1]
                arr.append(temp)
        return arr
