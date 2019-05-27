

def quick_sort(arr):
    if len(arr) < 2:  # 基线条件
        return arr
    else:
        pivot = arr[0]  # 递归条件，基准值
        less = [i for i in arr if i < pivot]
        greatest = [i for i in arr if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greatest)


if __name__ == '__main__':
    print(quick_sort([10, 5, 2, 3]))