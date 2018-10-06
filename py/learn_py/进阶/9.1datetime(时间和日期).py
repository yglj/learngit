# 1.获得当前时间和日期
from datetime import datetime  #datetime模块下datetime类(有时区)
print(datetime.now())

#2.创建一个日期时间
d1 = datetime(2018,4,19,12,20)
print(d1)

#3.timestamp 1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time
#当前时间等于epoch time 的秒数  datetime -> timestamp

print(d1.timestamp()) #返回一个浮点数，精确到毫秒

#4.timestamp -> datetime  utc标准时区
t = 1726611600.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))


#5.datetime转换为str,str转为datetime
print(d1.strftime('%Y-%m-%d %H-%M-%S'))
print(datetime.strptime('2018-04-19 12-20-00','%Y-%m-%d %H-%M-%S'))

#6.datetime 加减法  timedelta类
from datetime import timedelta
print(datetime.now()+timedelta(days=0,hours=40000))

#7.时区转化
from datetime import timezone
utc = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc)
print(utc.astimezone(timezone(timedelta(hours=8))))

import re
def to_timestamp(dt_str, tz_str):
    zone = re.match(r'UTC([+-]?\d{1,2})\:(\d){2}',tz_str).group(1)
    print(zone)
    ts = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    ts = ts.replace(tzinfo=timezone(timedelta(hours=int(zone))))
    return ts.timestamp()


##def to_timestamp(dt_str, tz_str):
##    cday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
##    utc_int=int(re.match(r'^UTC([+-]*\d+)\:\d+$',tz_str).group(1))
##    dt=cday.replace(tzinfo=timezone(timedelta(hours=utc_int)))
##    return (dt.timestamp())
# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
