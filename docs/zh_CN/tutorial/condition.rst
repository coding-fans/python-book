..
    Author: fasion
    Created time: 2020-03-16 20:13:34
    Last Modified by: fasion
    Last Modified time: 2020-03-21 22:24:46

.. meta::
    :description lang=zh:
    :keywords: python, 教程, 入门, 基础, 菜鸟, 条件判断, if, else, elif

===============
Python 条件判断
===============

考试成绩出来了，同学们都考得怎么样呢？心里不禁忐忑起来。

老师说，成绩达到 *60* 分或以上的才及格，不及格的童鞋要完成额外布置的作业！！！
那么，怎么让 *Python* 帮我们判断成绩是不是及格呢？

if 语句
=======

我们可以用 *if* 语句来判断某个成绩是否及格，示例程序如下：

.. literalinclude:: /_src/tutorial/condition/whether-pass.py
    :language: python
    :linenos:

第 *10* 行中的 *if* 语句意思是：如果变量 *score* 的值大于等于 *60* 就执行 *if* 下面的代码块。
代码块只有一行代码，即 *print* 语句，将字符串 ``成绩及格！`` 输出到屏幕。

注意到，代码块比 *if* 缩进了 *4* 个空格。
*Python* 以缩进区分不同代码块，这跟其他主流编程语言略有差异。
缩进可以是空格，也可以是制表符，同一代码块缩进必须一致。

小明这次考了 *85* 分，大于等于 *60* 条件成立，程序将如我们所料，输出 ``成绩及格！`` ：

.. code-block:: shell-session

    $ python whether-pass.py
    请输入分数：85
    成绩及格！

小刚这次只考了 *55* 分，不满足大于等于 *60* 的条件，因此没有输出 ``成绩及格！`` ：

.. code-block:: shell-session

    $ python whether-pass.py
    请输入分数：55

if 语法结构
===========

现在，回过头来研究 *if* 语句的语法结构。

计算机只能读懂编程语言，无法理解自然语言，我们只能通过编程语言与计算机交互。
从这个角度看，编程就像翻译——将任务翻译成编程语言，再交给计算机来执行。

汉语、英语等自然语言都有一定的语法结构，编程语言也有自己的语法。
与自然语言相比，编程语言规则更加简单，但也更加严格，错一个符号都不行。

那么， *Python* 这种编程语言的语法结构是怎样的呢？
我们以 *if* 为起点，开始学习：

.. figure:: /_images/tutorial/condition/761edd878643e26832d88b5f8ca0ad24.png

如上图， *if* 语句是由以下 *3* 个部分构成有机整体：

- *if* **关键词** ( *keyword* )，它标志着一个 *if* 语句的开始，还有其他关键字在等着我们；
- **判断条件** ( *condition* )，这是一个逻辑表达式，可求值为 **真** ( *true* )或 **假** ( *false* )；
- **真分支** ( *true branch* )，这是一个代码块，当条件成立(表达式求值为真)时才执行；

请注意，条件表达式后面有一个英文冒号 ``:`` 。
此外，代码块必须缩进，可以是一个 **空格** 或者 **制表符** 。
如果代码块里有多条语句， *Python* 将按照从上往下的顺序依次执行。

当条件表达式求值为 **真** 时， *Python* 先执行真分支代码块，再接着执行下面的语句，如绿色箭头所示。
当条件表达式求值为 **假** 时， *Python* 跳过真分支代码块，直接执行下面的语句，如红色箭头所示。

.. figure:: /_images/tutorial/condition/5fcd46532e730e668245b18751491f55.webp
    :width: 360px

逻辑表达式
==========

**逻辑表达式** ( *logic expression* )是一种求值结果是 **布尔值** ( *boolean value* )的表达式。
布尔只有两种值，要么为 **真** ( *true* )，要么为 **假** ( *false* )。
如果表达式成立，求值结果为真；否则，求值结果为假。

例如， ``1 < 2`` 成立，因此 *Python* 判断为 *True* ：

.. code-block:: python

    >>> 1 < 2
    True

这里小于号 ``<`` 是一个 **比较操作符** ( *comparison operator* )，对两个操作数进行比较，返回布尔值，表明比较关系是否成立。
``2 < 2`` 由于比较不成立， *Python* 判断为 *False* ：

.. code-block:: python

    >>> 2 < 2
    False

小明考了 *85* 分，大于等于 *60* 分成立，因此及格：

.. code-block:: python

    >>> score = 85
    >>> score >= 60
    True

小刚只考了 *55* 分，大于等于 *60* 分不成立，也就不及格了：

.. code-block:: python

    >>> score = 55
    >>> score >= 60
    False

if-else 语句
============

如果想在成绩及格时输出 ``成绩及格！`` ，不及格时输出 ``成绩不及格！`` ，有办法做到吗？

当然了，我们可以用 *if-else* 语句，程序示例如下：

.. literalinclude:: /_src/tutorial/condition/pass-or-not.py
    :language: python
    :linenos:

*if-else* 语句比 *if* 多了一个 *else* 分支，即 **假分支** ， 假分支在条件不成立时才执行。

小刚成绩只有 *55* 分，不满足大于等于 *60* 这个条件。
因此， *Python* 选择执行假分支，即第 *13* 处的代码块，向屏幕输出 ``成绩不及格！`` 字样。

.. code-block:: shell-session

    $ python pass-or-not.py
    请输入分数：55
    成绩不及格！

if-else 语法结构
================

*if-else* 语句是 *if* 语句的扩展，包含一个 *else* 分支，由以下 *5* 个部分组成：

.. figure:: /_images/tutorial/condition/8e556101bb9b43a00dd325c6baee8b7a.png

- *if* **关键词** ( *keyword* )，同 *if* 语句；
- **判断条件** ( *condition* )，同 *if* 语句；
- **真分支** ( *true branch* )，同 *if* 语句；
- *else* **关键词** ( *keyword* )，标志着假分支的开始；
- **假分支** ( *false branch* )，当条件不成立(条件表达式求值为 **假** )时才执行的代码块；

请特别注意， *else* 关键词后面同样需要一个英文冒号 ``:`` 。

if-elif-else 语句
=================

现在，老师想根据成绩为同学们计算等级，分为 *4* 档：

- 优秀，成绩 *90* 分或以上；
- 良好，成绩 *70* 分或以上；
- 及格，成绩 *60* 分或以上；
- 不及格，成绩达不到 *60* 分；

等级计算需要判断多个条件，相对复杂些，用一个流程图来表示更清晰：

.. figure:: /_images/tutorial/condition/755637ea7b53648f78032cff2fbe408a.svg
    :width: 600px

那么， *Python* 有办法实现这种同时包含多个条件的判断吗？
答案是肯定的， *if-elif-else* 语句闪亮登场！
成绩等级计算程序可以这样来写：

.. literalinclude:: /_src/tutorial/condition/show-level.py
    :language: python
    :linenos:

*if-elif-else* 同时包含多个判断条件，第一条件以 *if* 关键字开头，其余条件均以 *elif* 开头。
每个判断条件都关联着一个真分支，包含条件成立时需要执行的代码块。
*Python* 依次对每个条件进行检查，一旦某个条件成立便执行对应的代码块，其余条件则不再检查。
如果所有条件均不成立， *Python* 将执行 *else* 分支，即假分支的代码。

由于小军考了 *95* 分满足第一个条件， *Python* 输出 ``优秀`` ，不再检查其余条件了：

.. code-block:: shell-session

    $ python show-level.py
    请输入分数：95
    优秀

而小刚只有 *55* 分， *Python* 逐个检查判断条件，均不成立，便只好输出 ``不及格`` 了：

.. code-block:: shell-session

    $ python show-level.py
    请输入分数：55
    不及格

#. *55* 大于 *90* 是否成立？ 👉 不成立；
#. *55* 大于 *70* 是否成立？ 👉 不成立；
#. *55* 大于 *60* 是否成立？ 👉 不成立；
#. 执行 *else* 分支，输出不及格；

if-elif-else 语法结构
=====================

*if-elif-else* 语句是 *if-else* 语句的扩展，可以包括若干个 *elif* 分支，结构如下：

.. figure:: /_images/tutorial/condition/3f6deeb783d1d135880a8dd6776814aa.png

- *if* **关键词** ( *keyword* )，标志着第一个判断条件的开始；
- **判断条件** ( *condition* )，同 *if* 语句；
- **真分支** ( *true branch* )，同 *if* 语句；
- *elif* **关键词** ( *keyword* )，标志着另一个判断条件的开始；
- *else* **关键词** ( *keyword* )，同 *if-else* 语句；
- **假分支** ( *false branch* )，同 *if-else* 语句；

同样请注意，每个条件表达式后都有一个英文冒号 ``:`` 。

练习
====

学校修改了成绩等级规则，现划分为 *5* 个等级，分别如下：

- 卓越，成绩 *90* 分或以上；
- 优秀，成绩 *80* 分或以上；
- 良好，成绩 *70* 分或以上；
- 及格，成绩 *60* 分或以上；
- 不及格，成绩不足 *60* 分；

请动动手指，帮老师修改程序，以适应新等级划分规则。

附录
====

.. include:: /_fragments/appendix.rst

参考文献
========

#. `Python if else elif Statement <https://www.learnbyexample.org/python-if-else-elif-statement/>`_

.. include:: /_fragments/disqus.rst
