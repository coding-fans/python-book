..
    Author: fasion
    Created time: 2020-03-12 19:08:41
    Last Modified by: fasion
    Last Modified time: 2020-03-14 11:07:22

.. meta::
    :description lang=zh:
        编者担任Python面试官多年，积累了很多面试题，特整理起来，希望对求职者有所帮助。
        此外，我们从网上摘录了很多经典面试题，配以详尽的讲解，举一反三。
    :keywords: python, 面试题, 大全, 精讲

=================
Python 面试题精选
=================

编者担任 *Python* 面试官多年，积累了很多面试题，特整理起来，希望对求职者有所帮助。
此外，我们从网上摘录了很多经典面试题，配以详尽的讲解，举一反三。

我们将不定期更新，订阅可以关注我们的公众号： **小菜学编程** 。

面试题
======

#. **用一行代码实现整数 1 至 100 之和**

    网上的答案是通过 *range* 生成 *1* 至 *100* 的整数，然后用 *sum* 求和：

    .. code-block:: python

        >>> # 解法一
        >>> sum(range(1, 101))
        5050

    这行代码确实很有美感，但你想过没有：如果是求 *1* 至 *10000000000* 之和呢？
    候选人必须认识到这是一个 *O(N)* 算法，真的适合所有场景吗？为什么不用等差数列前 *N* 项和公式进行计算呢？

    .. code-block:: python

        >>> # 解法二
        >>> n = 100
        >>> (n + 1) * n >> 1
        5050

    采用前 *N* 项和公式，求和时间复杂度是 *O(1)* ，孰优孰劣应该很明显了吧。
    大家可以对比下当 *N* 很大时，这两种计算方式的表现：

    .. code-block:: python

        >>> n = 100000000
        >>> sum(range(1, n+1))
        5000000050000000
        >>> (n + 1) * n >> 1
        5000000050000000

    面试官喜欢引申，候选人如果只是刷题记答案而不会分析，肯定是过不了关的。

#. **如何在一个函数内部修改全局变量**

    在函数内部用 *global* 关键字将变量申明为全局，然后再进行修改：

    .. code-block:: python

        >>> a = 1
        >>> def func():
        ...     global a
        ...     a = 2
        ...
        >>> print(a)
        1
        >>> func()
        >>> print(a)
        2

    面试官还可能引申到以下概念讨论，必须滚瓜烂熟：

    - **变量作用域** ( *scope* )
    - **局部名字空间** ( *locals* )
    - **闭包名字空间** ( *globals* )
    - **全局名字空间** ( *enclosing* )
    - **内建名字空间** ( *builtin* )

#. **列出 5 个 Python 标准库**

    这是一个开发性题目，面试官以考察候选人知识面以及学习深度为目的。
    必须结合自身情况，选择一些自己比较熟悉的标准库作答，面试官随时可能深入讨论。

    保险一点，可以回答一些常用但很浅显的，例如：

    - `re`_ ，正则表达式处理
    - `datetime`_ ，日期时间处理
    - `json`_ ， *JSON* 数据处理
    - `math`_ ， 数学计算
    - `random`_ ， 随机数

    想要获得加分，也可以回答一些高级的，例如：

    - `os`_ ，系统调用
    - `socket`_ ，套接字编程与网络通讯
    - `threading`_ ，多线程处理
    - `multiprocessing`_ ，多进程处理
    - `queue`_ ，同步任务队列

    面试官很有很能深入提问，切记：如果自己不是很熟悉，就不要班门弄斧了。

#. **字典如何删除键**

    - 方法一，使用 *del* 语句进行删除， *del* 关键字还可用于删除 **变量** 、 **属性**

        .. code-block:: python

            >>> ages = {'tom': 18, 'jim': 20, 'lily': 19}
            >>> del ages['jim']
            >>> ages
            {'tom': 18, 'lily': 19}

    - 方法二，调用 *pop* 方法进行删除，这样可以拿到被删除键对应的值：

        .. code-block:: python

            >>> ages = {'tom': 18, 'jim': 20, 'lily': 19}
            >>> jims_age = ages.pop('jim')
            >>> jims_age
            20
            >>> ages
            {'tom': 18, 'lily': 19}

#. **如何合并两个字典**

    .. code-block:: python

        >>> info1 = {'name': 'jim', 'age': 18}
        >>> info2 = {'name': 'jim', 'score': 95}

    - 方法一，调用 *dict* 对象 *update* 方法：

        .. code-block:: python

            >>> info1.update(info2)
            >>> info1
            {'name': 'jim', 'age': 18, 'score': 95}

    - 方法二：

        .. code-block:: python

            >>> info = {**info1, **info2}
            >>> info
            {'name': 'jim', 'age': 18, 'score': 95}

#. **Python 2 和 Python 3 中的 range(100) 的区别**

    *Python 2* 中的 *range* 函数返回一个列表，长度越大消耗内存越多：

    .. code-block:: python

        >>> print(range(10))
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    *Python 2* 中的 *xrange* 函数与 *range* 类似，但返回 **生成器** ：

    .. code-block:: python

        >>> r = xrange(10)
        >>> ri = iter(r)
        >>> next(ri)
        0
        >>> next(ri)
        1

    生成器内存消耗固定，与长度无关。因此，循环一般使用 *xrange* ：

    .. code-block:: python

        >>> for i in range(10000):
        ...     pass
        ...

    由于生成器比较高效， *Python 3* 的 *range* 函数也选择返回生成器，可以认为与 *Python 2* 中的 *xrange* 等价：

    .. code-block:: python

        >>> r = range(10)
        >>> ri = iter(r)
        >>> next(ri)
        0
        >>> next(ri)
        1

    当然了，*Python 3* 中也可以实现与 *Python 2* 中的 *range* 函数一样的效果：

    .. code-block:: python

        >>> list(range(10))
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#. **Python 列表如何去重**

    .. code-block:: python

        >>> l = [7, 3, 0, 3, 0, 8, 4, 9, 3, 8]

    先将列表转换成 **集合** ( *set* )，由于集合元素不重复，便实现去重：

    .. code-block:: python

        >>> set(l)
        {0, 3, 4, 7, 8, 9}

    最后再将集合转化成列表即可：

    .. code-block:: python

        >>> list(set(l))
        [0, 3, 4, 7, 8, 9]

#. **一句话解释什么样的语言能够用装饰器**

    函数可以 **作为参数传递** 、 **可以作为返回值返回** 的语言，都可以实现装饰器。

#. **Python 内建数据类型有哪些**

    - **布尔** ， *bool*
    - **整数** ， *int*
    - **浮点** ， *float*
    - **字符串** ， *str*
    - **字节序列** ， *bytes*
    - **元组** ， *tuple*
    - **列表** ， *list*
    - **字典** ， *dict*

    面试官可进一步延伸到对象 **内部结构** ，相关操作 **时间复杂度** 等高级知识点。

#. **请编写正则表达式，提取以下网页中所有 a 标签的 URL**

    .. code-block:: html

        <html>
          <head>
            <title>小菜学编程</title>
          </head>
          <body>
            <ul>
              <li><a href="https://python.fasionchan.com">Python语言小册</a></li>
              <li><a href="https://linux.fasionchan.com">学习Linux</a></li>
              <li><a href="https://network.fasionchan.com">Linux网络编程</a></li>
              <li><a href="https://golang.fasionchan.com">Go语言小册</a></li>
              <li><a href="https://nodejs.fasionchan.com">Node.js小册</a></li>
            </ul>
          </body>
        </html>

    这题目考察标准库 *re* 模块的基本用法，难度不高，根据文本特征写正则即可：

    .. code-block:: python

        >>> import re
        >>> re.findall(r'<a.*href="([^"]+)".*>', page)
        ['https://python.fasionchan.com', 'https://linux.fasionchan.com', 'https://network.fasionchan.com', 'https://golang.fasionchan.com', 'https://nodejs.fasionchan.com']

    注意到，参考答案中的正则表达式匹配 *a* 开标签，括号表示 **内容提取** 。
    正则表达式在日常开发中应用场景很多，必须完全掌握。

#. **Python 中有几个名字空间，分别是什么**

    *Python* 总共有 *4* 个名字空间：

    - **局部名字空间** ( *locals* )
    - **闭包名字空间** ( *globals* )
    - **全局名字空间** ( *enclosing* )
    - **内建名字空间** ( *builtin* )


附录
====

.. include:: /_fragments/next-step-to-wechat-mp.rst

参考文献
========

#. `110道Python面试题（真题） - 知乎 <https://zhuanlan.zhihu.com/p/54430650>`_

.. include:: /_fragments/wechat-reward.rst

.. include:: /_fragments/disqus.rst

.. _re: https://docs.python.org/3/library/re.html
.. _datetime: https://docs.python.org/3/library/datetime.html
.. _math: https://docs.python.org/3/library/math.html
.. _random: https://docs.python.org/3/library/random.html
.. _json: https://docs.python.org/3/library/json.html

.. _os: https://docs.python.org/3/library/os.html
.. _threading: https://docs.python.org/3/library/threading.html
.. _multiprocessing: https://docs.python.org/3/library/multiprocessing.html
.. _queue: https://docs.python.org/3/library/queue.html
.. _socket: https://docs.python.org/3/library/socket.html
