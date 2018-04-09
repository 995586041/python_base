from datetime import datetime

# 获取当前日期和时间
now = datetime.now()
print(now)
print(type(now))
print(now.astimezone())

# 获取指定日期和时间
dt1 = datetime(2018, 4, 8, 16, 2, 8)
print(dt1)

# datetime转换为timestamp
# Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数
dt2 = datetime(2018, 4, 8, 16, 2, 8)
dt3 = datetime.now()
print(dt2.timestamp())
print(dt3.timestamp())

# timestamp转换为datetime
t = 1523174528.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))

# str转换为datetime
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
dt4 = datetime.strptime('2018:04-08 16:18:00', '%Y:%m-%d %H:%M:%S')
print(dt4)

# datetime转换为str
dt5 = datetime.now()
print(dt5.strftime('%Y:%m-%d %H:%M:%S'))

# 加减时间
from datetime import timedelta

# datetime加减
dt6 = datetime.now()
print(dt6)
print(dt6 + timedelta(hours=2))
print(dt6 + timedelta(weeks=1))

# 转换时区
from datetime import timezone

# 本地时间转换为UTC时间
tz_utc_8 = timezone(timedelta(hours=8))
tz_utc__8 = timezone(timedelta(hours=-8))

print(tz_utc_8)
print(tz_utc__8)
print(datetime.now().replace(tzinfo=tz_utc_8))

# 时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(utc_dt)
print(bj_dt)
print(tokyo_dt)
print(tokyo_dt2)

# work
str = '2015-1-21 9:01:30'
dt7 = datetime.strptime(str+"+0500", '%Y-%m-%d %H:%M:%S%z')
print('---------------')
print(dt7)
print(datetime.timestamp(dt7))
bj_dt = dt7.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
