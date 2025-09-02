# Count the pairs of (i,j), such that
# i < j, s[i] = 'a', s[j] = 'g'

# Brute force
def countAGPairs(s):
  N = len(s)
  count = 0

  for i in range(N-1):
    if s[i] == 'a':
      for j in range(i+1, N):
        if s[j] == 'g':
          count += 1
  return count

def main():
  S = "abegag"
  print(countAGPairs(S))
  
if __name__ == "__main__":
  main()
