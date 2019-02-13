.. 打包分发Python程序
    FileName:   binary-release.rst
    Author:     Fasion Chan
    Created:    2019-02-01 19:30:10
    @contact:   fasionchan@gmail.com
    @version:   $Id$

    Description:

    Changelog:

.. meta::
    :description lang=zh:
        运行Python程序，需要部署Python执行环境并安装依赖包，操作繁琐。
        借助PyInstaller等工具，可以将Python程序和Python环境一起打包成可执行程序，极大改善部署体验。
        本文以一个简单的实验程序，演示打包方法。
    :keywords: python, pyinstaller, 二进制, 打包

==================
打包分发Python程序
==================

运行 `Python` 程序，需要部署 `Python` 执行环境并安装依赖包，操作繁琐。

借助 `PyInstaller`_ 等工具，可以将 `Python` 程序和 `Python` 环境一起打包成可执行程序，
极大改善部署体验。
本文以一个简单的实验程序，演示打包方法。

实验程序
========

我们编写一个程序，并用它演示如何打包 `Python` 程序。
程序通过 `ntplib`_ 查询 `NTP` **服务器** 并输出相关信息：

.. literalinclude:: /_src/practices/binary-release/checktime.py
    :language: python
    :lines: 16-

先使用 `virtualenv` 初始化一个 `Python` 隔离环境进行实验：

.. code-block:: shell-session

    $ virtualenv env

验证 `Python` 隔离环境功能是否正常：

.. code-block:: shell-session

    $ env/bin/python --version
    Python 3.7.1

接着执行 `pip` 工具安装依赖包：

.. code-block:: shell-session

    $ env/bin/pip install ntplib==0.3.3

可以通过 `python` 命令执行程序了：

.. code-block:: shell-session

    $ env/bin/python checktime.py
    Server: 119.160.254.155
    Offset: 0.004868745803833008
    Time: 2019-02-01 19:34:17

PyInstaller
===========

.. figure:: /_images/practices/binary-release/3b69fba0e9d9577ba7b7f2746a61516b.png
    :width: 500px

`PyInstaller` 工具用于将 `Python` 应用及其依赖打包成一个 **单文件程序** 。支持系统包括：

- `Windows`
- `GNU/Linux <https://learn-linux.readthedocs.io/zh_CN/latest/>`_
- `Mac OS X <https://osx-guide.readthedocs.io/zh_CN/latest/>`_
- `FreeBSD`
- `Solaris`
- `AIX`

使用之前，需进行安装：

.. code-block:: shell-session

    $ env/bin/pip install pyinstaller==3.4

执行 `pyinstaller` 命令， `checktime.py` 是待打包脚本， `-F` 表示打包成单文件程序：

.. code-block:: shell-session

    $ env/bin/pyinstaller -F checktime.py

如无意外，在 `dist` 目录下可以找到打包后的程序。可以直接执行：

.. code-block:: shell-session

    $ dist/checktime
    Server: 42.204.179.159
    Offset: -0.024485349655151367
    Time: 2019-02-01 10:51:08

将以上程序拷贝到其他同类型系统上，也可以 **直接执行** 。
这样一来，其他系统无需安装 `Python` 环境，也无需安装依赖库即可执行 `Python` 应用，非常便捷！

下一步
======

.. include:: /_fragments/next-step-to-wechat-mp.rst

.. include:: /_fragments/wechat-reward.rst

.. include:: /_fragments/disqus.rst

.. _ntplib: https://pypi.org/project/ntplib/

.. comments
    comment something out below

