# Swap function
def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


# Selection sort function which select the smallest element in list and swap
def selection_sort(array):
    for i in range(0, len(array)):
        ismalest = i
        for j in range(i+1, len(array)):
            if array[j] < array[ismalest]:
                ismalest = j
        swap(array, i, ismalest)


# declaring list and calling selection sort algorithm
array = [22,11,33,88,55,66,77]
selection_sort(array)
print(array)
