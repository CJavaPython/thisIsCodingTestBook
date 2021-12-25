from sys import stdin
N=int(stdin.readline())
loc=[1,1]
plan=list(stdin.readline().split())
for dir in plan:
    if dir == "R":
        if loc[1]==N:
            continue
        loc[1] += 1
    elif dir == "L":
        if loc[1]==1:
            continue
        loc[1] -= 1
    elif dir == "U":
        if loc[0]==1:
            continue
        loc[0]-=1
    elif dir == "D":
        if loc[0]==N:
            continue
        loc[0]+=1

print(loc[0], loc[1])