#knight movement
#vertical 2 horizon 1 / horizon 1 vertical 2  (move like L)
#8*8 chess board(horizon : 1~8 / vertical a*h)
#input : knight location
loc = input()
#ord : char to integer
#ascii <a> = 97
hor = ord(loc[0]) - 97
ver = int(loc[1]) - 1
move = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]
result = 0
for i in range(len(move)):
    if hor + move[i][0] >= 0 and hor + move[i][0] <= 7 and ver + move[i][1] >= 0 and ver + move[i][1] <= 7:
        result += 1

print(result)
