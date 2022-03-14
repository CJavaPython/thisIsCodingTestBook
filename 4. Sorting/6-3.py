#Insertion Sorting
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    #first no skip, last skip(< <= / > >=)
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:#when it meets smaller than itself
            break

#if array almost sorted, it works very fast
#best : O(N)
#worst : O(n^2)