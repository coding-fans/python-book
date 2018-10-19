.. 部署方案
    FileName:   index.rst
    Author:     Fasion Chan
    Created:    2018-05-29 20:59:40
    @contact:   fasionchan@gmail.com
    @version:   $Id$

    Description:

    Changelog:

.. meta::
    :keywords: python, deploy, virtualenv, pip, requirements.txt, python deploy, python部署

========
部署方案
========

.. toctree::
    :titlesonly:

    pip 配置 <pip-conf>

`Python` 版本繁多， `Python` 应用需要依赖一些包，版本也不尽相同。
如果在系统级 `Python` 环境部署应用，可以预想到，一定存在冲突风险。
试想一下场景：

应用 `A` 、 `B` 均依赖一个数据库连接包，版本分别是 `a` 和 `b` ，两个版本有些不兼容。
如果两个应用部署在同个 `Python` 环境，那么数据库包应该安装什么版本呢？

独立部署环境
============

问题只能通过部署独立的 `Python` 环境来解决。那么同台机器如何部署多个 `Python` 环境呢？
甚至是版本不同的 `Python` 环境？—— `virtualenv`_ ！

首先，初始化一个新的 `Python` 环境：

.. code-block:: shell-session

    $ virtualenv ~/python
    New python executable in /Users/fasion/python/bin/python
    Installing setuptools, pip, wheel...done.

完成之后，便可启动 `Python` 解析器了：

.. code-block:: shell-session

    $ ~/python/bin/python
    Python 3.6.4 (default, Jan  6 2018, 11:51:59)
    [GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> print('abc')
    abc
    >>>

自然也可以用这个独立的环境来跑应用了：

.. code-block:: shell-session

    $ ~/python/bin/python /some/path/to/app.py

当然了，也可以指定 `Python` 版本：

.. code-block:: shell-session

    $ virtualenv -p python3 ~/python3

.. tip::

    用 `virtualenv`_ 制作独立的 `Python` 环境，对其任何操作均不影响其他环境。

依赖管理
========

`Python` 通过 `pip`_ 命令安装依赖包，大家应该都知道：

.. code-block:: shell-session

    $ pip install Flask

依赖包版本也很重要，用了错误版本的包可能导致应用异常。保险起见，装包时指定版本：

.. code-block:: shell-session

    $ pip install Flask==1.0.2

每次部署应用时，检查所有依赖包及版本是否就绪。
方法非常简单，直接运行装包命令即可。
`pip` 将确保依赖包以指定版本安装。

此外，最好可以通过配置文件将所有依赖保存下来。
`pip` 命令也支持依赖配置文件 `requirements.txt` ，内容格式如下：

.. code-block:: text

    Flask==1.0.2
    Jinja2==2.10

这样一来，一个命令就可以完成所有依赖包的安装：

.. code-block:: shell-session

    $ pip install -r requirements.txt

.. tip::

    应用在 `requirements.txt` 配置文件维护所有依赖包及版本并通过 `pip`_ 命令安装。

下一步
======

.. include:: /_fragments/next-step-to-wechat-mp.rst

.. include:: /_fragments/wechat-reward.rst

.. include:: /_fragments/disqus.rst

.. _pip: https://pip.pypa.io/
.. _virtualenv: https://virtualenv.pypa.io/

.. comments
    comment something out below

