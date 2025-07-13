# Closest MinMax

# Given an array A, find the size of the smallest subarray such that it
# contains at least one occurrence of the maximum value of the array
# and at least one occurrence of the minimum value of the array.

def main():
  A = [2, 6, 1, 6, 9]
  print("Smallest Subarray:", end = " ")
  print(minMax(A))

def minMax(A):
  N = len(A)
  min_val = min(A)
  max_val = max(A)

  # print(f"Min Value: {min_val}. Max Value: {max_val}")

  for i in range(N):
    if A[i] == min_val:
      for j in range(i, N):
        if A[j] == max_val:
          return j - i + 1

if __name__ == "__main__":
  main()



'''
N = len(A)
min_val = min(A)
max_val = max(A)
min_length = N

for i in range(N):
        for j in range(i + 1, N):
            if (A[i] == min_val and A[j] == max_val) or (A[i] == max_val and A[j] == min_val):
                current_length = j - i + 1

                if current_length < min_length:
                    min_length = current_length

return min_length
'''
