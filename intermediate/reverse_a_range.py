# Take a single line input  
A = list(map(int, input().split()))
print(A)

# First value is the length remove it
N = A.pop(0)
print(N)
print(A)

# reverse the list
A.reverse()

#print the reversed list without brackets and comma
print(*A)
