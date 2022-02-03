#정수 N 입력 -> N시 59분 59초까지 숫자 3이 하나라도 포함된 모든 경우의 수 구하기
x = int(input())

def func(num):
    result = 0
    for i in range(num+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    result+=1
    return result

print(func(x))
