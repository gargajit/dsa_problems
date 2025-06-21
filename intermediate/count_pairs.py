# Given an array A and an integer B. 
# A pair(i, j) in the array is a good pair if i != j and (A[i] + A[j] == B). 
# Check if any good pair exist or not.
# Return 1 if good pair exist otherwise return 0.

def main():
  A = [1,2,3,4]
  B = 7
  check_good_pair(A, B)


def check_good_pair(A, B):
  good_pair = set()
  
  for item in A:
      if B - item in good_pair:
          return 1
      else:
          good_pair.add(item)
      
  return 0


if __name__ == "__main__":
  main()
