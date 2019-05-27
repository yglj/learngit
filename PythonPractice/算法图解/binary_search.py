
def binary_search(array, x):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        elif array[mid] > x:
            high = mid - 1
    return None


if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9]
    result = binary_search(my_list, -1)
    print('result: %s' % result)
