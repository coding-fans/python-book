.. Python装饰器高级用法
    FileName:   advanced-decorator.rst
    Author:     Fasion Chan
    Created:    2018-10-29 08:30:31
    @contact:   fasionchan@gmail.com
    @version:   $Id$

    Description:

    Changelog:

.. meta::
    :description lang=zh:
    :keywords: python装饰器, 高级, python decorator, advanced, python装饰器高级用法, 闭包

====================
Python装饰器高级用法
====================

在 `Python` 中， **装饰器** 一般用来修饰函数，实现公共功能，达到代码复用的目的。
在函数定义前加上 `@xxxx` ，然后函数就注入了某些功能，很神奇！
然而，这只是 **语法糖** 而已，起决定性作用的其实是 **闭包** 。

场景
====

假设，有一些工作函数，用来对数据做不同的处理：

.. code-block:: python

    def work_bar(data):
        pass

    def work_foo(data):
        pass

我们想在函数调用前后输出日志，怎么办？

傻瓜解法
========

.. code-block:: python

    logging.info('begin call work_bar')
    work_bar(1)
    logging.info('call work_bar done')

如果有多处代码调用呢？想想就怕！

函数包装
========

傻瓜解法无非是有太多代码冗余，每次函数调用都要写一遍 `logging` 。
可以把这部分冗余逻辑封装到一个新函数里：

.. code-block:: python

    def smart_work_bar(data):
        logging.info('begin call: work_bar')
        work_bar(data)
        logging.info('call doen: work_bar')

这样，每次调用 `smart_work_bar` 即可：

.. code-block:: python

    smart_work_bar(1)

    # others...

    smart_work_bar(some_data)

通用闭包
========

看上去挺完美……
然而，当 `work_foo` 也有同样的需要时，还要再实现一遍 `smart_work_foo` 吗？
这样显然不科学呀！

别急，我们可以用 **闭包** ：

.. code-block:: python

    def log_call(func):
        def proxy(*args, **kwargs):
            logging.info('begin call: {name}'.format(name=func.func_name))
            result = func(*args, **kwargs)
            logging.info('call done: {name}'.format(name=func.func_name))
            return result
        return proxy

这个函数接收一个函数对象(被代理函数)作为参数，返回一个代理函数。
调用代理函数时，先输出日志，然后调用被代理函数，调用完成后再输出日志，最后返回调用结果。
这样，不就达到通用化的目的了吗？——对于任意被代理函数 `func` ， `log_call` 均可轻松应对。

.. code-block:: python

    smart_work_bar = log_call(work_bar)
    smart_work_foo = log_call(work_foo)

    smart_work_bar(1)
    smart_work_foo(1)

    # others...

    smart_work_bar(some_data)
    smart_work_foo(some_data)

第 `1` 行中， `log_call` 接收参数 `work_bar` ，返回一个代理函数 `proxy` ，并赋给 `smart_work_bar` 。
第 `4` 行中，调用 `smart_work_bar` ，也就是代理函数 `proxy` ，先输出日志，然后调用 `func` 也就是 `work_bar` ，最后再输出日志。
注意到，代理函数中， `func` 与传进去的 `work_bar` 对象紧紧关联在一起了，这就是 **闭包** 。

再提一下，可以覆盖被代理函数名，以 `smart_` 为前缀取新名字还是显得有些累赘：

.. code-block:: python

    work_bar = log_call(work_bar)
    work_foo = log_call(work_foo)

    work_bar(1)
    work_foo(1)

语法糖
======

先来看看以下代码：

.. code-block:: python

    def work_bar(data):
        pass
    work_bar = log_call(work_bar)


    def work_foo(data):
        pass
    work_foo = log_call(work_foo)

虽然代码没有什么冗余了，但是看是去还是不够直观。这时候，语法糖来了~~~

.. code-block:: python

    @log_call
    def work_bar(data):
        pass

因此，注意一点( **划重点啦** )，这里 `@log_call` 的作用只是：
告诉 `Python` 编译器插入代码 `work_bar = log_call(work_bar)` 。


求值装饰器
==========

先来猜猜装饰器 `eval_now` 有什么作用？

.. code-block:: python

    def eval_now(func):
        return func()

看上去好奇怪哦，没有定义代理函数，算装饰器吗？

.. code-block:: python

    @eval_now
    def foo():
        return 1

    print foo

这段代码输出 `1` ，也就是对函数进行调用求值。
那么到底有什么用呢？直接写 `foo = 1` 不行么？
在这个简单的例子，这么写当然可以啦。来看一个更复杂的例子——初始化一个日志对象：

.. code-block:: python

    # some other code before...

    # log format
    formatter = logging.Formatter(
        '[%(asctime)s] %(process)5d %(levelname) 8s - %(message)s',
        '%Y-%m-%d %H:%M:%S',
    )

    # stdout handler
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(formatter)
    stdout_handler.setLevel(logging.DEBUG)

    # stderr handler
    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setFormatter(formatter)
    stderr_handler.setLevel(logging.ERROR)

    # logger object
    logger = logging.Logger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(stdout_handler)
    logger.addHandler(stderr_handler)

    # again some other code after...

用 `eval_now` 的方式：

.. code-block:: python

    # some other code before...

    @eval_now
    def logger():
        # log format
        formatter = logging.Formatter(
            '[%(asctime)s] %(process)5d %(levelname) 8s - %(message)s',
            '%Y-%m-%d %H:%M:%S',
        )

        # stdout handler
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(formatter)
        stdout_handler.setLevel(logging.DEBUG)

        # stderr handler
        stderr_handler = logging.StreamHandler(sys.stderr)
        stderr_handler.setFormatter(formatter)
        stderr_handler.setLevel(logging.ERROR)

        # logger object
        logger = logging.Logger(__name__)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(stdout_handler)
        logger.addHandler(stderr_handler)

        return logger

    # again some other code after...

两段代码要达到的目的是一样的，但是后者显然更清晰，颇有独立 **代码块** 的风范。
更重要的是，函数调用在局部名字空间完成初始化，避免临时变量(如 `formatter` 等)污染外部的名字空间(比如全局)。

带参数装饰器
============

定义一个装饰器，用于记录慢函数调用：

.. code-block:: python

    def log_slow_call(func):
        def proxy(*args, **kwargs):
            start_ts = time.time()
            result = func(*args, **kwargs)
            end_ts = time.time()

            seconds = start_ts - end_ts
            if seconds > 1:
            logging.warn('slow call: {name} in {seconds}s'.format(
                name=func.func_name,
                seconds=seconds,
            ))

            return result

        return proxy

第 `3` 、 `5` 行分别在函数调用前后采样当前时间，第 `7` 行计算调用耗时，耗时大于一秒输出一条警告日志。

.. code-block:: python

    @log_slow_call
    def sleep_seconds(seconds):
        time.sleep(seconds)

    sleep_seconds(0.1)  # 没有日志输出

    sleep_seconds(2)    # 输出警告日志

然而，阈值设置总是要视情况决定，不同的函数可能会设置不同的值。如果阈值有办法参数化就好了：

.. code-block:: python

    def log_slow_call(func, threshold=1):
        def proxy(*args, **kwargs):
            start_ts = time.time()
            result = func(*args, **kwargs)
            end_ts = time.time()

            seconds = start_ts - end_ts
            if seconds > threshold:
                logging.warn('slow call: {name} in {seconds}s'.format(
                    name=func.func_name,
                    seconds=seconds,
                ))

            return result

        return proxy

然而， `@xxxx` 语法糖总是以被装饰函数为参数调用装饰器，也就是说没有机会传递 `threshold` 参数。
怎么办呢？——用一个闭包封装 `threshold` 参数：

.. code-block:: python

    def log_slow_call(threshold=1):
        def decorator(func):
            def proxy(*args, **kwargs):
                start_ts = time.time()
                result = func(*args, **kwargs)
                end_ts = time.time()

                seconds = start_ts - end_ts
                if seconds > threshold:
                logging.warn('slow call: {name} in {seconds}s'.format(
                    name=func.func_name,
                    seconds=seconds,
                ))

                return result

            return proxy

        return decorator


    @log_slow_call(threshold=0.5)
    def sleep_seconds(seconds):
        time.sleep(seconds)

这样， `log_slow_call(threshold=0.5)` 调用返回函数 `decorator` ，函数拥有闭包变量 `threshold` ，值为 `0.5` 。
`decorator` 再装饰 `sleep_seconds` 。

采用默认阈值，函数调用还是不能省略：

.. code-block:: python

    @log_slow_call()
    def sleep_seconds(seconds):
        time.sleep(seconds)

处女座可能会对第一行这对括号感到不爽，那么可以这样改进：

.. code-block:: python

    def log_slow_call(func=None, threshold=1):
        def decorator(func):
            def proxy(*args, **kwargs):
                start_ts = time.time()
                result = func(*args, **kwargs)
                end_ts = time.time()

                seconds = start_ts - end_ts
                if seconds > threshold:
                logging.warn('slow call: {name} in {seconds}s'.format(
                    name=func.func_name,
                    seconds=seconds,
                ))

                return result

            return proxy

        if func is None:
            return decorator
        else:
            return decorator(func)

这种写法兼容两种不同的用法，用法 `A` 默认阈值(无调用)；用法 `B` 自定义阈值(有调用)。

.. code-block:: python

    # Case A
    @log_slow_call
    def sleep_seconds(seconds):
        time.sleep(seconds)


    # Case B
    @log_slow_call(threshold=0.5)
    def sleep_seconds(seconds):
        time.sleep(seconds)

用法 `A` 中，发生的事情是 `log_slow_call(sleep_seconds)` ，也就是 `func` 参数是非空的，这时直接调 `decorator` 进行包装并返回(阈值是默认的)。

用法 `B` 中，先发生的是 `log_slow_call(threshold=0.5)` ， `func` 参数为空，直接返回新的装饰器 `decorator` ，关联闭包变量 `threshold` ，值为 `0.5` ；
然后， `decorator` 再装饰函数 `sleep_seconds` ，即 `decorator(sleep_seconds)` 。
注意到，此时 `threshold` 关联的值是 `0.5` ，完成定制化。

你可能注意到了，这里最好使用关键字参数这种调用方式——使用位置参数会很丑陋：

.. code-block:: python

    # Case B-
    @log_slow_call(None, 0.5)
    def sleep_seconds(seconds):
        time.sleep(seconds)

当然了， **函数调用尽量使用关键字参数** 是一种极佳实践，含义清晰，在参数很多的情况下更是如此。

智能装饰器
==========

上节介绍的写法，嵌套层次较多，如果每个类似的装饰器都用这种方法实现，还是比较费劲的(脑子不够用)，也比较容易出错。

假设有一个智能装饰器 `smart_decorator` ，修饰装饰器 `log_slow_call` ，便可获得同样的能力。
这样， `log_slow_call` 定义将变得更清晰，实现起来也更省力啦：

.. code-block:: python

    @smart_decorator
    def log_slow_call(func, threshold=1):
        def proxy(*args, **kwargs):
            start_ts = time.time()
            result = func(*args, **kwargs)
            end_ts = time.time()

            seconds = start_ts - end_ts
            if seconds > threshold:
            logging.warn('slow call: {name} in {seconds}s'.format(
                name=func.func_name,
                seconds=seconds,
            ))

            return result

        return proxy

脑洞开完， `smart_decorator` 如何实现呢？其实也简单：

.. code-block:: python

    def smart_decorator(decorator):

        def decorator_proxy(func=None, **kwargs):
            if func is not None:
                return decorator(func=func, **kwargs)

            def decorator_proxy(func):
                return decorator(func=func, **kwargs)

            return decorator_proxy

        return decorator_proxy

`smart_decorator` 实现了以后，设想就成立了！
这时， `log_slow_call` ，就是 `decorator_proxy` (外层)，
关联的闭包变量 `decorator` 是本节最开始定义的 `log_slow_call` (为了避免歧义，称为 `real_log_slow_call` )。
`log_slow_call` 支持以下各种用法：

.. code-block:: python

    # Case A
    @log_slow_call
    def sleep_seconds(seconds):
        time.sleep(seconds)

用法 `A` 中，执行的是 `decorator_proxy(sleep_seconds)` (外层)， `func` 非空， `kwargs` 为空；
直接执行 `decorator(func=func, **kwargs)` ，即 `real_log_slow_call(sleep_seconds)` ，结果是关联默认参数的 `proxy` 。

.. code-block:: python

    # Case B
    # Same to Case A
    @log_slow_call()
    def sleep_seconds(seconds):
        time.sleep(seconds)

用法 `B` 中，先执行 `decorator_proxy()` ， `func` 及 `kwargs` 均为空，返回 `decorator_proxy` 对象(内层)；
再执行 `decorator_proxy(sleep_seconds)` (内层)；最后执行 `decorator(func, **kwargs)` ，
等价于 `real_log_slow_call(sleep_seconds)` ，效果与用法 `A` 一致。

.. code-block:: python

    # Case C
    @log_slow_call(threshold=0.5)
    def sleep_seconds(seconds):
        time.sleep(seconds)

用法 `C` 中，先执行 `decorator_proxy(threshold=0.5)` ， `func` 为空但 `kwargs` 非空，返回 `decorator_proxy` 对象(内层)；
再执行 `decorator_proxy(sleep_seconds)` (内层)；最后执行 `decorator(sleep_seconds, **kwargs)` ，
等价于 `real_log_slow_call(sleep_seconds, threshold=0.5)` ，阈值实现自定义！

下一步
======

.. include:: /_fragments/next-step-to-wechat-mp.rst

.. include:: /_fragments/wechat-reward.rst

.. include:: /_fragments/disqus.rst

.. comments
    comment something out below

