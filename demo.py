# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

from datetimeLib import dt

sepa = '-' * 30

# 1. 返回当前日期或时间的属性
print('获取当前日期\t ==> ', dt.date)
print('获取当前时间\t ==> ', dt.time)
print('获取当前日期/时间\t ==> ', dt.datetime)
print('获取当前无格式日期\t ==> ', dt.dt)
print(sepa)

# 2. 返回当前日期或时间的方法
print('获取当前日期\t ==> ', dt.date_orm())
print('获取当前时间\t ==> ', dt.time_orm())
print('获取当前日期/时间\t ==> ', dt.datetime_orm())
print('获取当前无格式日期\t ==> ', dt.dt_orm())
print(sepa)

# 3. 日期时间和时间戳相互转换
print('获取当前时间戳\t ==> ', dt.timestamp)
print('日期/时间转时间戳 ==> ', dt.dt2ts(dt.datetime))
print('时间戳转日期/时间 ==> ', dt.ts2dt(dt.timestamp))
print(sepa)

# 4. 移动日期和时间
print('移动日期/时间[默认]\t ==> ', dt.move_dt())
print('移动日期/时间[前2天]\t ==> ', dt.move_dt(day=-2))
print('移动日期/时间[后3天]\t ==> ', dt.move_dt(day=3))
print('移动日期/时间[上月]\t ==> ', dt.move_dt(month=-1))
print('移动日期/时间[上周]\t ==> ', dt.move_dt(week=-1))
print('移动日期/时间[去年]\t ==> ', dt.move_dt(year=-1))
print('移动自定义日期/时间[上月]\t ==> ', dt.move_dt(sdt='2019-09-10 18:21:52', month=-1))
print('移动自定义日期/时间[去年]\t ==> ', dt.move_dt(sdt='2019-09-10', year=-1))
print('移动自定义日期/时间[上月-省略参数]\t ==> ', dt.move_dt('2019-09-10 18:21:52', month=-1))
print('移动自定义日期/时间[上月-指定类型]\t ==> ', dt.move_dt('2019-09-10 18:21:52', stp='datetime', month=-1))
print('移动自定义日期/时间[上个小时-指定类型]\t ==> ', dt.move_dt('2019-09-10 18:21:52', stp='time', hour=-1))
print(sepa)

# 5. 一个时间段内的连续日期列表
print('时间段内连续日期列表 ==> ', dt.list_dt('2019-08-29', '2019-09-02'))
print(sepa)

# 6. 格式转换
print('格式转换[-]\t ==> ', dt.format_dt('2019-09-10'))
print('格式转换[ ]\t ==> ', dt.format_dt('20190910'))

# 7. 休眠
dt.sleep(3)
