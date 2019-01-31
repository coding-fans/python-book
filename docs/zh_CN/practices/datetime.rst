.. 日期时间处理
    FileName:   datetime.rst
    Author:     Fasion Chan
    Created:    2018-12-03 18:20:40
    @contact:   fasionchan@gmail.com
    @version:   $Id$

    Description:

    Changelog:

.. meta::
    :description lang=zh:
    :keywords: python, datetime, last_month, last_week, 上周, 上月


============
日期时间处理
============

格式化
======

上周
====

如何判断上周是啥日期？以上周一为例：

.. code-block:: python
    :linenos:

    def get_this_monday():
        today = datetime.today()
        this_monday = (today - timedelta(days=today.weekday())).replace(
            hour=0,
            minute=0,
            second=0,
            microsecond=0,
        )
        return this_monday

    def get_last_monday():
        this_monday = get_this_monday()
        last_monday = this_monday - timedelta(days=7)
        return last_monday

函数 `get_this_monday` 获取本周一的日期，其中第 *2* 行取出当前日期时间；
第 *3-8* 行计算得到本周一。

函数 `get_last_monday` 获取上周一的日期，其中第 *12* 行获取本周一的日期；
第 *13* 行将其减去 *7* 天得到上周一。


上月
====

如何判断上月是何年何月？

可以将月减一，但对于一月份需要做特殊处理：则将年减一，月设置为 *12* ：

.. code-block:: python
    :linenos:

    import datetime

    def get_last_month():
        today = datetime.today()
        this_month = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        if this_month.month > 1:
            last_month = this_month.replace(month=this_month.month-1)
        else:
            last_month = this_month.replace(year=this_month.year-1, month=12)
        return last_month

第 *4* 行取出当前日期时间；
第 *5* 行将日期替换为 *1* 得到本月 *1* 号；
最后一个 *if* 语句判断本月是否为 **一月份** ，并据此分别进行处理。
这个方法简单粗暴，但是不是很优雅。

当然可以更优雅地处理：先将本月 *1* 号减去一天得到上个月最后一天；
接着将日期设置为 *1* 则得到上月 *1* 号。
代码如下：

.. code-block:: python
    :linenos:

    import datetime

    def get_last_month():
        today = datetime.today()
        this_month = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        last_month = (this_month - timedelta(days=1)).replace(day=1)
        return last_month

下一步
======

.. include:: /_fragments/next-step-to-wechat-mp.rst

.. include:: /_fragments/wechat-reward.rst

.. include:: /_fragments/disqus.rst

.. comments
    comment something out below

