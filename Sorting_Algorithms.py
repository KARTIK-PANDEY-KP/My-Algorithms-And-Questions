# 1. Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j>0 and arr[j-1]>temp:
            arr[j] = arr[j-1]
            j = j-1
        arr[j] = temp
    return arr

# Runner Code
arr = list(map(int, input().split(" ")))
print("sorted array is", insertion_sort(arr))
