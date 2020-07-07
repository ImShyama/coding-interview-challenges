## Sorting algorithm
In python we have a inbuilt function .sort to sort a list but,
we still have some algorithm to sort the list Or array.

* Insertion sort
* Selection sort
* Bubble sort

### 1. Insertion sort
Insertion sort algorithm sort array by swapping one by one 
and inserting the right element at the right position. 

```buildoutcfg
def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            swap(array, j-1, j)
            j -= 1
```

### 2. Selection sort
Selection sort algorithm sorts an array by repeatedly finding the minimum element, swap them from beginning of an array and sort them as ascending order.  
```buildoutcfg
def selection_sort(array):
    for i in range(0, len(array)):
        ismalest = i
        for j in range(i+1, len(array)):
            if array[j] < array[ismalest]:
                ismalest = j
        swap(array, i, ismalest)
```
### 3. Bubble sort
In bubble sort algorithm, with every complete iteration the largest element in the giver array, bubbles up towards the last place or the highest index.
```buildoutcfg
def bubble_sort(array):
    n = len(array) - 1
    for i in range(len(array)):
        for j in range(n):
            if array[j] > array[j+1]:
                swap(array, j, j+1)
        n -= 1

```