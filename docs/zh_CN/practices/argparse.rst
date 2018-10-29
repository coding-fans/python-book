.. 处理命令行参数
    FileName:   argparse.rst
    Author:     Fasion Chan
    Created:    2018-03-10 15:53:31
    @contact:   fasionchan@gmail.com
    @version:   $Id$

    Description:

    Changelog:

==============
处理命令行参数
==============

在程序开发中，经常需要调整程序的执行行为。

大部分情况下，最佳实践是—— **实现规范的命令行参数** ，而不是动不动就改代码。
试想一下，程序配置文件是通过命令行指定好呢？还是写死在代码里好呢？

每个程序都应该实现 ``-h`` 或者 ``--help`` 参数选项，输出帮助信息。
这样一来，谁都可以通过该途径获悉程序用法，应用自如。
这便是惯例的力量！

实现命令行参数的成本也不高，大部分语言都提供了足够方便的程序库，无需也不推荐重复造轮子：

`Python <https://www.python.org/>`_ 程序可以通过标准库 `argparse <https://docs.python.org/3/library/argparse.html>`_ 解析命令行参数。

快速上手
========

接下来，以一个名为 `AgentX` 的程序为例，讲解如何使用 `argparse <https://docs.python.org/3/library/argparse.html>`_ 模块。
`AgentX` 的用法如下：

.. code-block:: shell-session

    $ python agentx.py -h
    usage: agentx [-h] [-c conf_path] action

    positional arguments:
      action                action to carry out: status/start/stop

    optional arguments:
      -h, --help            show this help message and exit
      -c conf_path, --conf conf_path
                            configuration file path

``-h`` 选项显示帮助文档； ``-c`` 选项指定配置文件目录；
位置参数 ``action`` 指定要执行的操作。

借助 `argparse <https://docs.python.org/3/library/argparse.html>`_ ，解析命令行参数只需代码若干：

.. literalinclude:: /_src/practices/argparse/agentx.py
    :caption:
    :name: practices/argparse/agentx.py
    :language: python
    :linenos:

代码看似很长，但参数解析部分却只有一小段。

第 ``19`` - ``57`` 行是服务控制类 ``ServiceController`` 定义，我们需要根据命令行参数驱动该类执行选定逻辑。

紧接着是 ``main`` 函数定义，命令行解析逻辑代码所在。

``68`` 行处先初始化一个参数解析器， ``prog`` 参数是程序名字。

``82`` 行处是 ``-c`` 参数的定义： ``dest`` 执行参数值存放位置；
``metavar`` 是选项名称占位符，与 ``help`` 结合在帮助文档中显示；
``default`` 是默认值； ``required`` 指定选项是否必填。

``82`` 行处是位置参数 ``action`` 的定义：
``nargs`` 指定参数个数，这里为 ``1`` ；
``choices`` 指定参数可选值。

``91`` 行处调用解析器进行解析；``94`` 行处从解析结果中取值。
注意到，属性名和参数定义中 ``dest`` 参数一致。

总结起来，参数解析只需要这几个步骤：

#. 初始化解析器；
#. 定义选项；
#. 调用解析器解析参数；
#. 从解析结果取值；

下一步
======

.. include:: /_fragments/next-step-to-wechat-mp.rst

.. include:: /_fragments/wechat-reward.rst

.. include:: /_fragments/disqus.rst
