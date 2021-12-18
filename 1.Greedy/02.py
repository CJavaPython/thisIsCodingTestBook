N, M, K = map(int, input().split(" "))
L = list(map(int, input().split(" ")))
def bigNum(N, M, K, L):
  result = []
  max_index = L.index(max(L))
  max_val = L.pop(max_index)
  if M > K:
    for i in range(K):
      result.append(max_val)
    M -= K + 1
    next_max_val = L[L.index(max(L))]
    result.append(next_max_val)
    L.insert(max_index, max_val)
    result.extend(bigNum(N, M, K, L))
  else:
    for i in range(M):
      result.append(max_val)
  return sum(result)
print(bigNum(N, M, K, L))
