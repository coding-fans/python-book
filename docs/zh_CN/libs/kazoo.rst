.. kazoo
    FileName:   kazoo.rst
    Author:     Fasion Chan
    Created:    2019-01-14 15:55:55
    @contact:   fasionchan@gmail.com
    @version:   $Id$

    Description:

    Changelog:

.. meta::
    :description lang=zh:
        kazoo是一个更优雅的Zookeeper库，用法更简单，也不容易出错。
        本文介绍kazoo的一些典型用法，并提供代码示例。
    :keywords: python, kazoo, zookeeper

=====
kazoo
=====

`kazoo`_ 是一个更优雅的 `Zookeeper`_ 库，用法更简单，也不容易出错。

安装
====

开始使用 `kazoo`_ 之前，你需要先装好它。推荐从 `PYPI`_ 安装：

.. code-block:: shell-session

    $ pip install kazoo

连接处理
========

建立连接
--------

开始操作 `Zookeeper`_ 之前，需要先创建 `KazooClient`_ 对象并与 `Zookeeper` 建立连接：

.. code-block:: python

    from kazoo.client import KazooClient

    zk = KazooClient(hosts='127.0.0.1:2181')
    zk.start()

默认，客户端通过本地端口( *2181* )连接 `Zookeeper` 服务器。
这种情况下，需要先确保 `Zookeeper` 已在本地运行，否则 `start` 方法将一直等待直到超时。

一旦成功连接，客户端会尝试保持连接状态，自动处理 **间歇性连接中断** 以及 **会话过期** 等问题。
如果需要放弃当前连接，需要调用 `stop` 方法：

.. code-block:: python

    zk.stop()

鉴权
----

如果 `Zookeeper` 设置了用户密码，则需要额外指定：

.. code-block:: python

    zk = KazooClient(
        hosts='127.0.0.1:2181',
        auto_data=[
            ('digest', 'user:password'),
        ],
    )

监听连接事件
------------

掌握连接状态非常重要，用户需要知晓 **连接中断** 、 **重连** 以及 **会话过期** 等事件。
为了简化处理逻辑， `kazoo`_ 将其抽象成一个状态系统。
用户可以在上面注册监听函数，监听函数在连接状态发生变化时得到调用。

.. code-block:: python

    from kazoo.client import KazooState

    def my_listener(state):
        if state == KazooState.LOST:
            # 连接丢失
        elif state == KazooState.SUSPENDED:
            # 连接断开
        else:
            # 连接建立或重连

    zk.add_listener(my_listener)

在使用 `kazoo.recipe.lock.Lock`_ 或者创建临时节点等场景，
强烈建议添加状态监听函数，以便程序在连接中断或者会话丢失时可以正确应对。

理解连接状态
------------

日志设置
--------

如果应用代码未设置 `logging` ，则可能出现以下错误信息：

.. code-block:: text

    No handlers could be found for logger "kazoo.client"

为了避免这个问题，你可以添加以下两行代码：

.. code-block:: python

    import logging
    logging.basicConfig()

增删改查
========

读取数据
--------

相关方法：

- *exists()* ，检查路径节点是否存在；
- *get()* ，读取节点数据以及节点详情信息( `ZnodeStat` 对象)；
- *get_children()* ，获取指定节点下所有子节点；

判断路径节点是否存在：

.. code-block:: python

    if zk.exists('/path/to/given/node'):
        # do something

读取节点数据以及版本：

.. code-block:: python

    data, stat = zk.get('/path/to/given/node')
    print('Version:', stat.version)
    print('Data:', data.decode('utf-8'))

列举子节点：

.. code-block:: python

    children = zk.get_children('/path/to/given/node')
    for child in children:
        print('Child:', child)

下一步
======

.. include:: /_fragments/next-step-to-wechat-mp.rst

参考文献
========

#. `Basic Usage — kazoo 2.6.0 documentation <https://kazoo.readthedocs.io/en/latest/basic_usage.html>`_

.. include:: /_fragments/wechat-reward.rst

.. include:: /_fragments/disqus.rst

.. _kazoo: https://kazoo.readthedocs.io/en/latest/index.html
.. _kazoo.recipe.lock.Lock: https://kazoo.readthedocs.io/en/latest/api/recipe/lock.html#kazoo.recipe.lock.Lock
.. _KazooClient: https://kazoo.readthedocs.io/en/latest/api/client.html#kazoo.client.KazooClient
.. _PYPI: https://pypi.org/
.. _Zookeeper: https://zookeeper.apache.org/

.. comments
    comment something out below

