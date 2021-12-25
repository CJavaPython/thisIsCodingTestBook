#from sys import stdin
#stdin.readline()

N, K = map(int, input().split())
count=0
count=N%K
while N>=K:
    N=int(N/K)
    count+=1
print(count)

# 슬래쉬 2개(//) : 몫    /     % : 나머지0