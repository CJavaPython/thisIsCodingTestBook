def recursion_function(i):
    #if print 100 times, terminate
    if i == 100:
        return
    print(i, "번째 재귀 함수에서 ", i+1, "번째 재귀 함수를 호출합니다.")
    recursion_function(i+1)
    print(i, "번째 재귀 함수를 종료합니다.")

recursion_function(1)