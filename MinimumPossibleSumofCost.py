# Given two arrays A and B
# The following operations can be performed in A and B
#   -> Shuffle values in B without changing the order of elements in A

# It is given that the cost of two arrays of same size is the sum of (product of values at same indices) across all indices.

# You can perform the operation any number of times.

# Find the minimum cost possible across all subarrays of A and B.

def solution(A,B,N):
  A.sort()
  B.sort(reverse=True)

  
  table = [[ 0 for i in range(N+1)] for j in range(N+1)]

  for i in range(1,N+1):
    table[i][i] = A[i-1] * B[i-1]

  for i in range(1,N):
    for j in range(1,N-i+1):
      table[j][j+i] = table[j][j+i-1] + table[j+1][j+i] - table[j+1][j+i-1]

  minimumSum = 0
  
  for row in table:
    minimumSum += sum(row)

  return minimumSum


N = int(input())

A = []
B = []

for _ in range(N):
  A.append(int(input()))

for _ in range(N):
  B.append(int(input()))

print(solution(A,B,N))
