.. IPy
    FileName:   ipy.rst
    Author:     Fasion Chan
    Created:    2018-05-31 20:05:51
    @contact:   fasionchan@gmail.com
    @version:   $Id$

    Description:

    Changelog:

.. meta::
    :keywords: python, ip block, ip, ip segment

===
IPy
===

`IPy <https://pypi.org/project/IPy/>`_ 是一个用来处理 `IP` 地址和网段的类库。

IP地址
======

`IP` 类用来表示 `IP` 地址， `IPv4` 和 `IPv6` 都支持。

.. code-block:: pycon

	>>> from IPy import IP
	>>> IP('10.0.0.0').version()
	4
	>>> IP('::1').version()
	6

可以判断 `IP` 类型：

.. code-block:: pycon

	>>> ip.iptype()
	'PRIVATE'

IP网络
======

通过 `IP` 表示一个网络，即相邻的多个 `IP` 地址：

.. code-block:: pycon

		>>> from IPy import IP
		>>> ip = IP('10.2.32.0/30')
		>>> ip.len()
		4
		>>> for x in ip:
		...     print(x)
		...
		10.2.32.0
		10.2.32.1
		10.2.32.2
		10.2.32.3

还可以通过掩码指定：

.. code-block:: pycon

		>>> ip = IP('10.2.32.0/255.255.255.252')

也可以直接指定范围：

.. code-block:: pycon

		>>> ip = IP('10.2.32.0-10.2.32.3')

这几种写法是等价的。

下一步
======

.. include:: /_fragments/next-step-to-wechat-mp.rst

.. include:: /_fragments/wechat-reward.rst

.. include:: /_fragments/disqus.rst

.. comments
	comment something out below

