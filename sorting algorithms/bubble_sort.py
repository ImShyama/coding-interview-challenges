# Swap function
def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


# bubble sort algorithm which automatically sort the last element in list so we decrease the second loop search length 'n'
def bubble_sort(array):
    n = len(array) - 1
    for i in range(len(array)):
        for j in range(n):
            if array[j] > array[j+1]:
                swap(array, j, j+1)
        n -= 1

# Declaring array and calling bubble_sort function
array = [100, 99, 88, 111, 110]
bubble_sort(array)
print(array)

