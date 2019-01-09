.. 疑难杂症
    FileName:   issues.rst
    Author:     Fasion Chan
    Created:    2019-01-08 19:04:50
    @contact:   fasionchan@gmail.com
    @version:   $Id$

    Description:

    Changelog:

.. meta::
    :description lang=zh:
        本文记录一些使用matplotlib过程中遇到的问题，以及针对问题的解决方案。
    :keywords: matplotlib, 常见问题, backend, framework, Agg, TkAgg, 椭圆

========
疑难杂症
========

本文记录一些使用 `matplotlib`_ 过程中遇到的 **问题** ，以及针对问题的 **解决方案** 。

backend
=======

在 `OSX`_ 下，用 `virtualenv` 提供的虚拟 `Python` 环境运行 `matplotlib` ，会抛异常：

.. code-block:: text

    ImportError: Python is not installed as a framework. The Mac OS X backend will not be able to function correctly if Python is not installed as a framework. See the Python documentation for more information on installing Python as a framework on Mac OS X. Please either reinstall Python as a framework, or try one of the other backends. If you are using (Ana)Conda please install python.app and replace the use of 'python' with 'pythonw'. See 'Working with Matplotlib on OSX' in the Matplotlib FAQ for more information.

关键信息是， `Python` 不是作为 `framework` 安装，因此找不到 `Mac OS X backend` 。
解决方法也非常简单，只需在使用 `matplotlib` 之前，先设置使用 `TkAgg` ：

.. code-block:: python

    import matplotlib
    matplotlib.use('TkAgg')

    import matplotlib.pyplot as plt

当然了，也可以将设置写到配置文件，一劳永逸：

.. code-block:: shell-session

    $ cat ~/.matplotlib/matplotlibrc
    backend: TkAgg

详情请参考文章：
`Python via virtualenv on Mac OS X: RuntimeError: Python is not installed as a framework. <https://markhneedham.com/blog/2018/05/04/python-runtime-error-osx-matplotlib-not-installed-as-framework-mac/>`_
。

圆形不圆
========

使用 `pyinstaller` 对程序进行打包后再运行，发现一个诡异的现象：
用 `pie` 方法画出的饼状图变成了一个椭圆！
同样的程序直接运行 `python` 命令运行是完全正常的，这太奇怪了！
应该是 `pyinstaller` 额外运行一些 `hook` 代码导致的，由于时间关系没细究。

为了解决这个问题，只需添加一行代码：

.. code-block:: python

    ax.set_aspect('equal')

详情请参考文章：
`Why is matplotlib plotting my circles as ovals? - Stack Overflow <https://stackoverflow.com/questions/9230389/why-is-matplotlib-plotting-my-circles-as-ovals>`_
。

参考文献
========

#. `Python via virtualenv on Mac OS X: RuntimeError: Python is not installed as a framework. <https://markhneedham.com/blog/2018/05/04/python-runtime-error-osx-matplotlib-not-installed-as-framework-mac/>`_
#. `Why is matplotlib plotting my circles as ovals? - Stack Overflow <https://stackoverflow.com/questions/9230389/why-is-matplotlib-plotting-my-circles-as-ovals>`_

.. _matplotlib: https://matplotlib.org
.. _OSX: https://osx-guide.readthedocs.io/zh_CN/latest/

.. comments
    comment something out below

