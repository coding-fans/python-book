..
    Author: fasion
    Created time: 2020-03-15 22:15:01
    Last Modified by: fasion
    Last Modified time: 2020-03-16 20:15:12

.. meta::
    :description lang=zh:
    :keywords: python, 教程, 入门, 基础, 菜鸟, 数学运算, 变量

========
数学运算
========

我们已经 *Python* 开发环境，并且成功运行第一个 *Python* 程序。
虽然程序只是在屏幕上打印一句话，但这只是第一步，我们还可以让计算机执行更高级的任务呢！

计算器
======

我们可以将 *Python* 当做计算器来用，让计算机做一些简单的数学运算。
打开 *Python* 终端，输入算式并按回车即可，例如计算 *1 + 1* 的值：

.. code-block:: python

    >>> 1 + 1
    2

不止加法，常用的数学运算符， *Python* 都支持：

.. code-block:: python

    >>> # 减法
    >>> 10 - 2
    8

    >>> # 乘法
    >>> 5 * 5
    25

    >>> # 除法
    >>> 1 / 4
    0.25

    >>> # 平方
    >>> 5 ** 2
    25

    >>> # 立方
    >>> 2 ** 3
    8

    # 乘方(10的10次方)
    >>> 10 ** 10
    10000000000

.. note::

    请注意，*#* 号开头表示 **注释** ， *Python* 将忽略注释内容。

运算符优先级
============

对于包含多个运算符的算式，计算顺序由运算符优先级决定。
小时候我们都知道，先算乘除，再算加减，同级按从左到右的顺序计算。

.. code-block:: python

    >>> 1 + 2 + 3
    6

这个式子先计算 *1 + 2* ，再将结果与 *3* 相加，等价于：

.. code-block:: python

    >>> 1 + 2
    3
    >>> 3 + 3
    6

而下面这个式子则先计算乘法，再跟前面的 *1* 相加：

.. code-block:: python

    >>> 1 + 10 * 10
    101

    >>> # 等价于
    >>> 10 * 10
    100
    >>> 1 + 100
    101

如果需要先计算加法，可以用括号将加法括起来：

.. code-block:: python

    >>> (1 + 10) * 10
    110

变量
====

现在，我们来做一些有意义的计算，例如计算圆的面积。
假设以 *3.14* 为圆周率，按圆面积计算公式 :math:`\pi r^2` 半径为 *1* 的圆面积可以这样计算：

.. code-block:: python

    >>> 3.14 * 1 ** 2
    3.14

这么简单不如口算得了，来点稍微复杂一点的：

.. code-block:: python

    >>> 3.14 * 1.5 ** 2
    7.065

如果以 *3.14159* 为圆周率，结果又是多少呢？

.. code-block:: python

    >>> 3.14159 * 1.5 ** 2
    7.0685775

由于圆周率是一个很长的常数，容易写错，我们可以用一个变量将它保存起来：

.. code-block:: python

    >>> pi = 3.14159

程序中的变量可以理解成一个保存着某个值的名字，通过 **变量名** 即可取出对应的 **值** 。
我们将变量 *pi* 的值打印到屏幕看看：

.. code-block:: python

    >>> print(pi)
    3.14159

这样一来，我们计算圆面积时便无须敲下长长的小数了，直接使用变量 *pi* 即可：

.. code-block:: python

    >>> pi * 1.5 ** 2
    7.0685775

变量，顾名思义，值是可以改变的。例如，我们可以将 *pi* 的值修改为 *3.14* ：

.. code-block:: python

    >>> pi = 3.14
    >>> pi
    3.14

现在，以新的圆周率，重新计算半径为 *1.5* 的圆的面积：

.. code-block:: python

    >>> pi * 1.5 ** 2
    7.065

顺便提一下，使用变量前必须先定义变量，否则程序将报错：

.. code-block:: python

    >>> pi2
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    NameError: name 'pi2' is not defined

附录
====

.. include:: /_fragments/next-step-to-wechat-mp.rst

.. include:: /_fragments/wechat-reward.rst

.. include:: /_fragments/disqus.rst
