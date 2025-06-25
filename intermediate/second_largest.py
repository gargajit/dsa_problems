# Second largest

def find_second_largest(A):
  largest = max(A)
  
  if A[0] < largest:
    second_largest = A[0]
  else:
    second_largest = -1

  for i in range(len(A)):
    if largest > A[i] > second_largest:
      second_largest = A[i]
  
  return second_largest

arr1 = [2, 1, 2]
arr2 = [2]
arr3 = [20,12,15,19,13,5,13,12,18]
arr4 = [1,2,3]

# find_second_largest(arr1)
# find_second_largest(arr2)
# find_second_largest(arr3)
find_second_largest(arr4)
