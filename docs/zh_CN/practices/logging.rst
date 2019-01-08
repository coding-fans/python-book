.. 日志输出
    FileName:   logging.rst
    Author:     Fasion Chan
    Created:    2019-01-07 19:55:21
    @contact:   fasionchan@gmail.com
    @version:   $Id$

    Description:

    Changelog:

.. meta::
    :description lang=zh:
        日志在问题分析时必不可少，好的程序应该输出足够的日志信息。
        那么，用Python语言开发程序时，如何输出日志呢？
    :keywords: python, logging, 日志输出, 日志格式, Logger, Handler, Formatter

========
日志输出
========

日志在问题分析时必不可少，好的程序应该输出足够的日志信息。

那么，用 `Python` 语言开发程序时，如何输出日志呢？

—— `logging`_ 模块！

.. code-block:: pycon

    >>> import logging
    >>> logging.warning('something wrong happended.')
    WARNING:root:Something wrong happended.
    >>> logging.info('seems good!')

这是一个入门级例子，导入 `logging`_ 模块后，调用 `warning` 方法即可输出警告信息。

日志级别
========

日志输出视轻重缓急，可分为多个级别。
例子还调用 `info` 方法输出一条普通信息，级别比警告信息低。
`Python` 支持的日志级别包括：

.. csv-table:: 表格-1 日志级别
    :header: "名称", "数值", "方法", "含义"

    "CRITICAL", "logging.CRITICAL", "logger.critical", "严重错误"
    "ERROR", "logging.ERROR", "logger.error", "错误"
    "WARNING", "logging.WARNING", "logger.warning", "警告"
    "INFO", "logging.INFO", "logger.info", "普通信息"
    "DEBUG", "logging.DEBUG", "logger.debug", "调试信息"
    "NOTSET", "logging.NOTSET", "", "未指定"

注意到，例子中 `info` 输出的普通信息并没有真正打印到屏幕上，
这是因为默认的 `logger`_ 对象只输出较高级别日志。
为了输出想要的级别，我们需要自行定制 `Logger`_ 对象。

日志对象
========

`Logger`_ 对象通过 `getLogger` 方法创建：

.. code-block:: pycon

    >>> logger = logging.getLogger(__name__)
    >>> logger.setLevel(logging.INFO)
    >>> logger.info('you must be able to see me!')
    INFO:__main__:you must be able to see me!

调用 `Logger`_ 对象 `setLevel` 方法设置日志输出级别，后续将忽略比该级别低的日志。
调用 `debug` 方法输出日志将被忽略：

.. code-block:: pycon

    >>> logger.debug('you cant see me now!')

更多定制方法，请查看 `帮助文档 <https://docs.python.org/3/library/logging.html#logger-objects>`_ ：

.. code-block:: pycon

    >>> help(logger)

日志处理器
==========

前面几个例子，日志均输出到标准输出，因此我们可以在屏幕中看到。
当然了，日志还可以输出到文件，甚至可以通过网络发送出去，这都是通过 `Handler`_ 对象控制的。

标准输出
--------

日志对象默认输出到标准输出，等价于：

.. code-block:: python

    logger_handler = logging.StreamHandler(sys.stdout)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logger_handler)

可以进一步控制处理器可以输出的 **日志级别** ：

.. code-block:: python

    logger_handler = logging.StreamHandler(sys.stdout)
    logger_handler.setLevel(logging.WARNING)

这样一来，只有不低于 `WARNING` 级别的日志才会被该处理器处理。
需要注意的是， `Logger`_ 对象以及 `Handler`_ 对象级别同时影响日志输出行为。

文件
----

相比标准输出，将日志输出到文件更为妥当，文件可以保留一定的历史待查。

日志格式
========

采用默认格式输出的日志非常丑陋，信息量也不够，甚至连时间都没有！
因此，需要根据应用需求，灵活调整日志输出格式。
为 `Handler` 对象自定义格式：

.. code-block:: python
    :linenos:

    import logging, sys

    FMT = '%(asctime)s %(levelname) 8s: [%(filename)s:%(lineno)d] [%(processName)s:%(process)d %(threadName)s] - %(message)s'
    DATEFMT = '[%Y-%m-%d %H:%M:%S]'

    logger_handler = logging.StreamHandler(sys.stdout)
    logger_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(fmt=FMT, datefmt=DATEFMT)
    logger_handler.setFormatter(formatter)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logger_handler)

关键代码是 `9-10` 行，初始化一个格式化器，并设置到 `Handler` 对象上。
初始化器需要两个参数， `fmt` 指定日志格式， `datefmt` 指定日期格式。
除了日志内容，日志记录可以注入 **时间** 、 **级别** 、 **代码文件名** 、
**代码行数** 、 **进程名** 、 **进程ID** 、 **线程名** 等信息。

例子输出大致如下，可以看到 **格式更为美观，信息更为丰富** 了：

.. code-block:: pycon

    >>> logger.info('Hello, world!')
    [2019-01-08 11:25:50]     INFO: [<stdin>:1] [MainProcess:99324 MainThread] - Hello, world!

下一步
======

.. include:: /_fragments/next-step-to-wechat-mp.rst

参考文献
========

#. `logging — Logging facility for Python <https://docs.python.org/3/library/logging.html>`_

.. include:: /_fragments/wechat-reward.rst

.. include:: /_fragments/disqus.rst

.. _logging: https://docs.python.org/3/library/logging.html
.. _Logger: https://docs.python.org/3/library/logging.html#logger-objects
.. _Handler: https://docs.python.org/3/library/logging.html#handler-objects

.. comments
    comment something out below

