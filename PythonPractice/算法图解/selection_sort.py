"""
快速排序
"""
import copy


def find_small(arr):
    small = arr[0]
    small_index = 0
    for i in range(len(arr)):
        if small > arr[i]:
            small = arr[i]
            small_index = i
    return small_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        n = find_small(arr)
        new_arr.append(arr.pop(n))
    return new_arr


def SeclectSort(arr):
    for j in range(len(arr)):
        k = j
        for i in range(j, len(arr)):
            if arr[i] < arr[k]:
                k = i
        temp = arr[j]
        arr[j] =  arr[k]
        arr[k] = temp
    print(arr)

if __name__ == '__main__':
    array = [5, 3, 6, 2, 10]
    arr = copy.copy(array)
    # arr = copy.deepcopy(array)
    print(selection_sort(array))
    SeclectSort(arr)