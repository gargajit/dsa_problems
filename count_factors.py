# Count the factors of N

def main():
  N = int(input("Enter the number N: "))
  factors = cnt_factors(N)
  print(f"The number of factors of {N}: {factors}")



def cnt_factors(N):
  cnt = 0
  i = 1

  while i * i <= N:
    if N % i == 0:
      if i == N/i:
        cnt += 1
      else:
        cnt += 2
    i += 1
  return cnt


if __name__ == "__main__":
  main()
