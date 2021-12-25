#N * M
N, M = map(int, input().split())
m = -1
for i in range(N):
    n = min(list(map(int, input().split())))
    m = max(m, n)
print(m)