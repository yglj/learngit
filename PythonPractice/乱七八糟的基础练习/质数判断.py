def su():
    num = int(input("enter:"))
    if num > 1:
        for i in range(2, num):
            if (num % i == 0):
                print(num, "不是质数")
                print(i, "*", num // i, "=", num)
                break
        else:
            print(num, "是质数")  # for...else
    else:
        print("不是质数")

def S():
    low = 1#int(input())
    high =100# int(input())
    for i in range(low, high+1):
        for j in range(2,i):
            if (i % j == 0 or i<1):
                break
        else:
            print(i, "是质数")  # for...else
S()