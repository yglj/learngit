
def countdown(i):
    if i <= 1:
        print(i)
    else:
        countdown(i-1)


def countSum(arr):
    if not arr:
        return 1
    else:
        return arr[0] * countSum(arr[1:])
    # elif i == 0:
    #     return arr[i]
    # return arr[i] * countSum(arr, i-1)


if __name__ == '__main__':
    alist = [1, 2, 3, 4, 5]
    print(countSum(alist))
