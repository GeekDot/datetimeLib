<h2 align= center> datetimeLib 增强日期时间库 </h2>

<h5 align=right> 张懿 </h5>
<p align=right> 2019-09-10 </p>

### 一、概述

`datetimeLib` 是增强版的日期时间库，依赖 `re`、`time`、`datetime`、`arrow` 库。`datetimeLib` 是对 `arrow` 库进行二次封装，使用更加方便简洁，只用一行就可以解决绝大部分的问题

下面是对 `datetimeLib` 的详解，如想快速使用，请移步 `demo.py` 模块，里面有 `datetimeLib` 的使用 `demo`

### 二、安装

`datetimeLib` 是以源码的方式呈现，使用的时候直接导入即可

	from datetimeLib import dt
    
### 三、使用

`datetimeLib` 所有的功能都是 `dt` 的属性或方法，它们的返回值都是 `string` 类型，`datetimeLib` 包括 `6` 类功能

1. 返回当前日期或时间

2. 日期时间和时间戳相互转换

3. 移动日期和时间

4. 一个时间段内的连续日期列表

5. 格式转换

6. 休眠

#### 1. 返回当前日期或时间

返回年
	
	dt.year
    
返回月

	dt.month

返回日

	dt.day

返回小时

	dt.hour

返回分钟

	dt.minute
	
返回秒
	
	dt.second
    
返回日期

	dt.date

返回时间

	dt.time

返回日期和时间

	dt.datetime
	
#### 2. 日期时间和时间戳相互转换

返回当前时间戳

	dt.timestamp

日期时间转时间戳

	dt.dt2ts(sdt)
	
参数 `sdt` 是必要参数，格式为：`'0000-00-00'` 或 `'0000-00-00 00:00:00'`

时间戳转日期时间

	dt.ts2dt(sts)
	
参数 `sts` 是必要参数，格式为：时间戳字符串

#### 3. 移动日期和时间

	dt.move_dt()

方法原型：

	move_dt(sdt=None, stp=None, year=0, month=0, day=0, hour=0, minute=0, second=0, week=0)
	
方法中有 `9` 个参数，其中两个功能参数 `sdt`、`stp`，其他都是针对时间和日期的操作，默认为 `0`，为 `0` 是默认为今天的日期和时间，传入正数是向后移动，如：`day=2`，向后移动 `2` 天（后天），传入负数是向前移动，如：`month=-1`，向前移动 `1` 个月（上月）

- `sdt`：`set datetime`，即传入日期时间，格式为：`'0000-00-00'` 或 `'0000-00-00 00:00:00'`，默认为当前日期时间

- `stp`：`set timestamp`，即设置返回日期时间类型，支持 `3` 中类型：`date`、`time`、`datetime`，默认为 `date`

- `year`：年

- `month`：月

- `day`：日

- `hour`：时

- `minute`：分

- `second`：秒

- `week`：周

#### 4. 一个时间段内的连续日期列表

	dt.list_dt()
	
例如输入：`'2019-09-06'` 和 `'2019-09-08'` 输出则为：`['2019-09-06', '2019-09-07', '2019-09-08']`
	
方法原型：

	list_dt(sdate=None, edate=None)

- `sdate` 开始时间，格式为：`'0000-00-00'`

- `edate` 结束时间，格式为：`'0000-00-00'`

#### 5. 格式转换

只针对最常用的 `'0000-00-00'` 和 `'00000000'` 格式相互转换，其他特殊格式根据所提供的功能全都可以灵活实现

	dt.format_dt(sdt)
	
参数 `sdt` 是必要参数，传入格式为 `'0000-00-00'` 或 `'00000000'`，类型为字符串型，如果格式错误将返回 `None`

#### 6. 休眠

	dt.sleep(sp=0)
	
`dt.sleep()` 是休眠时常，单位是秒，需要休眠是直接传入对应的秒数即可

	dt.sleep(3) # 休眠 3 秒
