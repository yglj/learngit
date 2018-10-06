'''
二分查找
'''

def binary_search(list,x):
    low = 0
    high = len(list)-1
    while low<=high:
        mid = (low + high) // 2
        if list[mid] == x:
            return x
        elif list[mid] < x:
            low = mid + 1
        elif list[mid] > x:
            high = mid - 1
    return None

if __name__ == '__main__':
    print(binary_search([1,2,4,7,9,25],4))
    print(binary_search([1,2,4,7,9,25],-3))