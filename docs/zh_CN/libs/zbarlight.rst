..
    Author: fasion
    Created time: 2018-11-19 10:30:21
    Last Modified by: fasion
    Last Modified time: 2020-03-07 21:09:20


=========
zbarlight
=========

`zbarlight <https://pypi.python.org/pypi/zbarlight>`_ 是 `zbar <http://zbar.sourceforge.net/>`_ 库的一个封装，可以方便地读取(识别)二维码内容。

安装
====

安装 `zbarlight` 之前，需要先安装 `zbar` 以及其头文件。
因此，安装方式因平台而异：

Debian
------

.. code-block:: shell

    sudo apt-get install libzbar0 libzbar-dev
    sudo pip install zbarlight

Mac OS X
--------

.. code-block:: shell

    brew install zbar
    export LDFLAGS="-L$(brew --prefix zbar)/lib"
    export CFLAGS="-I$(brew --prefix zbar)/include"
    pip install zbarlight

例子
====

.. literalinclude:: /_src/libs/zbarlight/read_qrcode.py
    :caption:
    :name: libs/zbarlight/read_qrcode.py
    :language: python
    :linenos:
    :lines: 16-29

这个例子非常简单：
第 ``8`` - ``10`` 行打开文件并加载二维码图片，
第 ``12`` 行调用 ``zbarlight`` 工具函数识别二维码。

下一步
======

.. include:: /_fragments/next-step-to-wechat-mp.rst

.. include:: /_fragments/wechat-reward.rst

.. include:: /_fragments/disqus.rst

.. comments
    comment something out below

    .. meta::
        :description lang=zh:
        :keywords:

