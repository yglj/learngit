# 逻辑运算

# 与（and）、 或（or）、 非（not）

is_employee = True
score = 0

if not is_employee:
    print('not employee')
else:                               # if...elif...else
    if score <= 60 and score >=0:
        print('dismiss')            # if判断
    elif score > 60 or score < 100:
        print('pass')
    else:
        pass