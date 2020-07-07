# swap function for swaping the array element
def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


# Insertion sort function which sort the array
def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            swap(array, j-1, j)
            j -= 1


# Creating list and calling insertion sort function
array = [11, 5, 10, 4, 6]
insertion_sort(array)
print(array)
