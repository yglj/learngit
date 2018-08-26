
year = int(input('请输入一个年份：'))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('%s是闰年'%year)
        else:
            print('%s不是闰年'%year)
    else:
            print('%s不是闰年'%year)
else:
            print('%s不是闰年'%year)




