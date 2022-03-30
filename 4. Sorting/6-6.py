#계수정렬 : count sort
#특정 조건에만 사용가능 but 빠름 (최악에도 O(N+K)) (데이터 개수 N, 최대값 K)
#특정 조건 : 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 가능 : 1,000,000정도일 떄 효과적임
#데이터 크기만큼을 가진 배열 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
result = [0 for _ in range(len(array))]
for i in array:
    result[i] = result[i] + 1
for i in range(len(result)):
    for j in range(result[i]):
        print(i, end=' ')