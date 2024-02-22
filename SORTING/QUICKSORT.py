def quickSort(arr, low, high):
    if low < high:
        partition_index = self.partition(arr, low, high)
        self.quickSort(arr, low, partition_index - 1)
        self.quickSort(arr, partition_index + 1, high)


'''The worst case of quicksort is when array is already sorted.'''
def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            arr[low], arr[j] = arr[j], arr[low]  # pivot swap
            return j

quickSort([2,-1,3,0,4,8,9],0,6)