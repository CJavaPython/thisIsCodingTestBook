N, K = map(int, input().split())
count=0
count=N%K
while N>=K:
    N=int(N/K)
    count+=1
print(count)