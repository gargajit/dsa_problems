class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def kthsmallest(self, A, B):
        # Convert the tuple into a list
        A = list(A)
        
        # Sort the list A
        A.sort()

        # Return the Bth smallest element ie, B-1 from the 0th index
        return A[B-1]


