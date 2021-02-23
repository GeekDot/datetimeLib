#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import re
import arrow
import time as _time


# 时间日期操作
class DatetimeLib(object):

    def __init__(self, timezone='+08:00'):
        self.tz = timezone

    # 返回年、月、日、时、分、秒的属性和方法
    def year(self):
        return str(arrow.now(self.tz).year)

    def month(self):
        return str(arrow.now(self.tz).month)

    def day(self):
        return str(arrow.now(self.tz).day)

    def hour(self):
        return str(arrow.now(self.tz).hour)

    def minute(self):
        return str(arrow.now(self.tz).minute)

    def second(self):
        return str(arrow.now(self.tz).second)

    # 返回日期的属性和方法
    def date(self):
        return str(arrow.now(self.tz).date())

    # 返回时间的属性和方法
    def time(self):
        return str(arrow.now(self.tz).time()).split('.')[0]

    # 返回日期时间的属性和方法
    def datetime(self):
        return str(arrow.now(self.tz).datetime).split('.')[0]

    # 返回无格式日期的属性和方法
    def dt(self):
        return str(arrow.now(self.tz).date()).replace('-', '')

    # 返回当前时间戳
    @staticmethod
    def timestamp():
        return int(arrow.now().timestamp)

    # 日期时间 <转> 时间戳
    def dt2ts(self, sdt):
        return int(arrow.get(sdt, tzinfo=self.tz).timestamp)

    # 时间戳 <转> 日期时间
    def ts2dt(self, sts):
        return str(arrow.get(sts, tzinfo=self.tz)).split('+')[0].replace('T', ' ')

    # 移动时间和日期 <sdt>:传入时间日期 <stp>:返回类型 <Other>:要移动的参数
    def move(self, sdt=None, stp=None, year=0, month=0, day=0, hour=0, minute=0, second=0, week=0):

        # sdt 默认为当前日期
        if sdt is None:
            sdt = self.datetime

        datetime = str(arrow.get(sdt, tzinfo=self.tz).shift(years=year, months=month, days=day, weeks=week, hours=hour,
                                                            minutes=minute, seconds=second)).split('+')[0].replace('T',
                                                                                                                   ' ')
        date = datetime.split(' ')[0]
        time = datetime.split(' ')[1]

        # tp 默认返回 date
        if stp == 'hydra_datetime':
            return datetime

        elif stp == 'time':
            return time

        else:
            return date

    # 一个时间段内的连续日期列表 ['2019-09-06', '2019-09-07', '2019-09-08']
    def list(self, start_date=None, end_date=None):

        if start_date is None and end_date is None:
            s_date = self.date
            e_date = self.date
        else:
            s_date = start_date
            e_date = end_date

        _s_date = arrow.get(s_date, tzinfo=self.tz)
        _e_date = arrow.get(e_date, tzinfo=self.tz)

        days = str(_e_date - _s_date).split(' ')[0]

        # 如果开始时间和结束时间是一样的，则会返回特殊字符，对特殊字符特殊处理
        if days == '0:00:00':
            days = 0
        else:
            days = int(days)

        date_list = []

        for day in range(days + 1):
            next_date = self.move(sdt=s_date, day=day)
            date_list.append(next_date)

        return date_list

    # 带格式日期时间相互转换
    @staticmethod
    def format(sdt):
        # 传入参数为 '2019-01-01' 格式
        if re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', sdt) is not None:
            return sdt.replace('-', '')
        # 传入参数为 '12:00:00' 格式
        elif re.match(r'^[0-9]{2}:[0-9]{2}:[0-9]{2}$', sdt) is not None:
            return sdt.replace(':', '')
        # 传入参数为 '2019-01-01 12:00:00' 格式
        elif re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}[ ][0-9]{2}:[0-9]{2}:[0-9]{2}$', sdt) is not None:
            return sdt.replace('-', '').replace(' ', '').replace(':', '')
        # 传入参数为 '20190101' 格式
        elif re.match(r'^[0-9]{8}$', sdt) is not None:
            return sdt[0:4] + '-' + sdt[4:6] + '-' + sdt[6:8]
        # 传入参数为 '120000' 格式
        elif re.match(r'^[0-9]{6}$', sdt) is not None:
            return sdt[0:2] + ':' + sdt[2:4] + ':' + sdt[4:6]
        # 传入参数为 '20190101120000' 格式
        elif re.match(r'^[0-9]{14}$', sdt) is not None:
            return sdt[0:4] + '-' + sdt[4:6] + '-' + sdt[6:8] + ' ' + sdt[8:10] + ':' + sdt[10:12] + ':' + sdt[12:14]
        # 格式错误返回 None
        else:
            return None

    # 休眠
    @staticmethod
    def sleep(sp=0):
        _time.sleep(sp)


dt = DatetimeLib()
