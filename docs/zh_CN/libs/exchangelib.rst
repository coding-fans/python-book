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

发送邮件
========

发送邮件只需初始化 `Message` 对象并调用 `send` 方法即可：

.. code-block:: python

    from exchangelib import Message

    message = Message(
        account=account,
        subject='测试主题',
        body='这是一封测试邮件',
        to_recipients=(
            'jim@example.com',
        ),
    )
    message.send()

其中， *account* 参数是账号授权信息，抢先一览小节已介绍过；
*subject* 为邮件主题； *body* 为邮件体；
*to_recipients* 指定收件人列表。

抄送、密送
----------

**抄送** 收件人列表通过 `cc_recipients` 参数指定：

.. code-block:: python

    message = Message(
        account=account,
        subject='测试主题',
        body='这是一封测试邮件',
        to_recipients=(
            'jim@example.com',
        ),
        cc_recipients=(
            'another-one@example.com',
        ),
    )

类似地， **密送** 收件人通过 `bcc_recipients` 参数指定：

.. code-block:: python

    message = Message(
        account=account,
        subject='测试主题',
        body='这是一封测试邮件',
        to_recipients=(
            'jim@example.com',
        ),
        bcc_recipients=(
            'another-one@example.com',
        ),
    )

HTML邮件
--------

邮件一般不局限于纯文本，可以用 `HTML` 编写格式丰富的内容：

.. code-block:: python

    from exchangelib import HTMLBody

    html = '<html><body>Hello happy <blink>OWA user!</blink></body></html>'
    message = Message(
        account=account,
        subject='测试主题',
        body=HTMLBody(html),
        to_recipients=(
            'jim@example.com',
        ),
    )

发送附件
--------

发送附件需要初始化 `FileAttachment` 对象，指定文件名以及文件内容，
并通过 `Message` 对象 *attach* 方法附着到邮件上：

.. code-block:: python

    from exchangelib import FileAttachment

    logo_filename = 'logo.png'
    with open(logo_filename, 'rb') as f:
        logo = FileAttachment(
            filename=logo_filename,
            content=f.read(),
        )
    message.attach(logo)
    message.send()

内嵌附件图片
------------

附件图片可以嵌到 `HTML` 邮件体中进行展示。
此时，需要为附件指定一个 `CID` ，以便在 `HTML` 中引用：

.. code-block:: python

    logo_filename = 'logo.png'
    with open(logo_filename, 'rb') as f:
        logo = FileAttachment(
            filename=logo_filename,
            content=f.read(),
            content_id=logo_filename,
        )
    message.attach(logo)
    message.body = HTMLBody('<html><body>Hello logo: <img src="cid:%s"></body></html>' % (logo_filename,))
    message.send()

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

