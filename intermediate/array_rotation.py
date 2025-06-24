# Array Rotation

#Problem Description
#Given an integer array A of size N and an integer B, you have to return the same array after rotating it B times towards the right.

def main():
  A = list(map(int, input("Enter the integer array: ").split()))
  B = int(input("Enter integer by which array will be rotated: "))

  print(rotate(A,B))


def rotate(A, B):
        N = len(A)
        B = B % N

        def reverse_it(arr, i, j):
            while i < j:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

                i += 1
                j -= 1
        
        reverse_it(A, 0, N-1)
        reverse_it(A, 0, B-1)
        reverse_it(A, B, N-1)

        return A

if __name__ == "__main__":
  main()
  
