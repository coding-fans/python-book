.. exchangelib
    FileName:   exchangelib.rst
    Author:     Fasion Chan
    Created:    2018-10-23 18:27:25
    @contact:   fasionchan@gmail.com
    @version:   $Id$

    Description:

    Changelog:

.. meta::
    :keywords: exchangelib, python, exchange mail, exchange邮件, exchange收发

===========
exchangelib
===========

`exchangelib`_ 是一个用于操作 `Exchange` 邮箱的第三方库，其接口设计简单易用。
类库现有功能如下：

- 服务器自动发现( `autodiscover` )
- 对象搜索( `searching` )
- 对象创建( `creating` )
- 对象更新( `updating` )
- 对象发送( `sending` )
- 对象删除( `deleting` )
- etc

抢先一览
========

下面这个例子仅用若干行代码便实现了打印输出收件箱前 `100` 封邮件：

.. code-block:: python

	from exchangelib import Credentials, Account

	credentials = Credentials('john@example.com', 'topsecret')
	account = Account('john@example.com', credentials=credentials, autodiscover=True)

	for item in account.inbox.all().order_by('-datetime_received')[:100]:
		print(item.subject, item.sender, item.datetime_received)

可以看到，将邮箱账号和密码传给 `exchangelib`_ 之后，即可通过简单的操作函数完成各种不可以思议的操作！

安装
====

开始使用 `exchangelib`_ 之前，你需要先装好它。推荐从 `PYPI`_ 安装：

.. code-block:: shell-session

	$ pip install exchangelib

默认的安装版本不支持 `Kerberos` 。
如果实在需要 `Kerberos` ，可以安装带 `Kerberos` 依赖的版本：

.. code-block:: shell-session

	$ pip install exchangelib[kerberos]

想要安装最新的代码，则可以直接从 `Github`_ 安装：

.. code-block:: shell-session

	$ pip install git+https://github.com/ecederstrand/exchangelib.git

.. warning::

    最新的代码可能不太稳定，在生产中使用需要谨慎测试验证。

此外，由于 `exchangelib` 用到 `lxml` 包以及用以支持 `Kerberos` 认证的 `pykerberos` 包，
你可能需要装一些额外的系统包，具体方法因操作系统而异。

对于 `Debian` 系列系统：

.. code-block:: shell-session

    $ apt-get install libxml2-dev libxslt1-dev

    $ # For Kerberos support, also install these:
    % apt-get install libkrb5-dev build-essential libssl-dev libffi-dev python-dev

对于 `CentOS` 系列系统：

.. code-block:: shell-session

    $ # For Kerberos support, install these:
    $ yum install gcc python-devel krb5-devel krb5-workstation python-devel


下一步
======

.. include:: /_fragments/next-step-to-wechat-mp.rst

.. include:: /_fragments/wechat-reward.rst

.. include:: /_fragments/disqus.rst

.. _exchangelib: https://pypi.org/project/exchangelib/
.. _PYPI: https://pypi.org/
.. _Github: https://github.com/ecederstrand/exchangelib

.. comments
    comment something out below

