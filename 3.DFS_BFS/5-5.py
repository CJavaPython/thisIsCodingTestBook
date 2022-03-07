#factorial 구현
#반복적 구현
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
#재귀적 구현
def factorial_recursive(n):
    if n<= 1:
        return 1
    return n * factorial_recursive(n-1)

print("반복적 구현 : ", factorial_iterative(5))
print("재귀적 구현 : ", factorial_recursive(5))
#결과는 같다
#재귀 함수가 더 간결 : 수학의 점화식 그대로 소스 코드로 옮겼기 때문 ==> dp로 이어진다.