#samsung implementation test
#map : N * M
#character location : (A, B)
#looking direction : d (0 : north, 1 : east, 2 : south, 3 : west)
#map's Sea vs Land (0 : Land, 1 : Sea)
map_size=list(map(int, input().split()))
A, B, d = map(int, input().split())
mapping=[]

map = []
for i in range(map_size[0]):
    #for j in range(map_size[1]):
    tmp = list(map(int, input().split()))
    map.append(tmp)
#1. look left direction
d=(d-1)%4
#2. if not going
