#quick sort : 재귀함수
#hoare partition : set first data as pivot
#평균 시간 복잡도 : O(NlogN) : 정확히 반씩 나눴을 때 길이는 N, 높이는 logN이기 때문
#worst : N제곱 : 데이터가 이미 정렬되어있는 경우 느리게 동작 (거의다 정렬됐을때 빠르게 동작하는 삽입정렬가 대비됨)
array = [5, 7 ,9 ,0 ,3 , 1 , 6 , 2, 4, 8]

def quick_sort(array, start, end):
    if start>=end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        #iterate while finding value bigger than pivot
        while left <= end and array[left] <= array[pivot]:
            left+=1
        #iterate while finding value smaller than pivot
        while right > start and array[right] >= array[pivot]:
            right-=1
        if left>right: #엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)