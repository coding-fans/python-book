.. 完美解决Python2的编码问题
    FileName:   py2-encoding.rst
    Author:     Fasion Chan
    Created:    2019-01-30 19:54:04
    @contact:   fasionchan@gmail.com
    @version:   $Id$

    Description:

    Changelog:

.. meta::
    :description lang=zh:
        将输出Unicode的Python程序重定向到文件，程序便抛异常，这是由编码问题导致的。
        找到问题症结后，可通过三种方法解决：
        一、设置PYTHONIOENCODING环境变量；
        二、替换 `sys.stdout` 文件对象，指定编码；
        三、重新设置程序默认编码方式。
    :keywords: python2, 编码, 乱码, UnicodeEncodeError, ascii, 标准输出, 重定向,

=========================
完美解决Python2的编码问题
=========================

背景
====

计算机无论 **存储信息** ，或者通过网络 **交换信息** ， **基本单位** 都是 **八位字节** ( `octet` )。
八位字节能够表示的字符数最多不超过 *256* 种：

.. math::
    2^8 = 256

这用来存储英文字母是绰绰有余，但是要满足全世界人民可就难了——汉字光常用的就几千个呢！
怎么办呢？——用多个字节存储呗。这时，全世界人民齐头并进：

- 中国人民使用 *GB2312* 、 *GBK* 、 *GB18030* ；
- 日本人民使用 *Shift JIS* 、 *EUC-JP* ；
- 韩国人民使用 *EUC_KR* ；
- *etc*

各家自扫门前雪， **互不兼容** 。直到有个老好人 `Unicode` 出来统一世界，收录人类所有字符。
`Unicode` 字符集非常庞大，也需要多个字节存储，最常见的编码方式是 `UTF-8` 。
因此，对于同一个汉字 **我** ，按不同的编码存储后的字节是不一样的：

.. csv-table:: 汉字与编码

    "汉字", "我"
    "Unicode", "25105"
    "GBK", "两字节：0xce 0xd2"
    "UTF-8", "三字节：0xe6 0x88 0x91"

一个 `GBK` 编码的字节序列，如果以 `UTF-8` 来读，肯定是一坨狗屎。
因此，知晓数据编码方式非常重要，直接关系到数据的解读。
中文编码方式有好几套，互不兼容，因此中文世界里的乱码现象就不难理解了。

在 `Python 2` ，字符分为两种，首先是 `Unicode` 字符：

.. code-block:: python

    u'你好，世界！'

普通字符串可以理解成字符序列：

.. code-block:: python

    '你好，世界！'

.. note::

    代码中的普通字符串编码与代码文件相同；交互式模式中输入时与终端编码相同。

在两种字符串之间转换，需要 **编码** 或者 **解码** ：

.. code-block:: python

    # 编码
    a = u'你好，世界！'
    b = a.encode('utf8')

    # 解码
    b.decode('utf8')

文件流
======

文件存储 **八位字节** ，不管待存数据是啥，最终要转化成字节。
那么，如果直接写入 `Unicode` 字符串，会发生什么事情：

.. code-block:: pycon

    >>> f = open('somefile.out', 'w+')
    >>> f.write(u'你好，世界！')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-5: ordinal not in range(128)

毫不意外，提示默认的 `ascii` 编码器不能编码待写入的数据。

但注意到，我们在终端运行程序，却可以输出 `Unicode` 字符串。
将以下代码保存成 `say-hello.py` 文件，并运行：

.. literalinclude:: /_src/practices/py2-encoding/say-hello.py
    :language: python
    :lines: 16-

.. code-block:: shell-session

    $ python2 say-hello.py
    你好，世界！

为啥呢？理论上， ``print`` 也是写到 `sys.stdout` 中，它也是一个文件对象呀！

然而，  `Python` 初学者还经常被另一个问题困扰，将输出重定向到文件就又不行了？

.. code-block:: shell-session

    $ python2 say-hello.py > /dev/null
    Traceback (most recent call last):
      File "say-hello.py", line 16, in <module>
          print u'你好，世界！'
          UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-5: ordinal not in range(128)

还记得吗， `Python` 打开文件有两种不同的模式， **文本模式** 和 **二进制模式** ：

.. code-block:: python

    # 文本模式
    f = open('somefile.out', 'w+')

    # 二进制模式
    f = open('somefile.out', 'wb+')

既然默认是文本模式，可以非常合理地怀疑 `sys.stdout` 文件对象的编码设置。
接下来，写一个程序 `stdio-encoding.py` 来检查在不同的运行方式下， 标准 *IO* 对象的编码方式：

.. literalinclude:: /_src/practices/py2-encoding/stdio-encoding.py
    :language: python
    :lines: 16-

直接运行，继承终端输入输出，文件对象的编码方式是 `UTF-8` (因环境而已)：

.. code-block:: shell-session

    $ python2 stdio-encoding.py
    stdin UTF-8
    stdout UTF-8
    stderr UTF-8

标准错误重定向， `stderr` 文件对象编码方式变成了 `None` ！

.. code-block:: shell-session

    $ python2 stdio-encoding.py 2>/dev/null
    stdin UTF-8
    stdout UTF-8
    stderr None

将标准输出写到管道，行为也是一样的！

.. code-block:: shell-session

    $ python2 stdio-encoding.py | cat
    stdin UTF-8
    stdout None
    stderr UTF-8

为啥继承终端输入输出， `Python` 可以给标准 `IO` 文件对象设置正确的编码呢？
这是因为 `Python` 可通过用户设置的环境变量获悉终端的编码方式：

.. code-block:: shell-session

    $ env | grep UTF
    LANG=en_US.UTF-8
    LC_ALL=en_US.UTF-8
    LC_CTYPE=UTF-8

至此，问题的症结已经对位到，解决方案也呼之欲出。

方法一：PYTHONIOENCODING 环境变量
---------------------------------

第一种解决方法是，通过环境变量，明确告诉 `Python` 进行 `IO` 的编码方式：

.. code-block:: shell-session

    $ PYTHONIOENCODING=UTF-8 python2 say-hello.py
    你好，世界！

还是原来的代码，设置 `PYTHONIOENCODING` 环境变量后程序成功运行了！

方法二：设置文件对象编码
------------------------

第二种方法，则是将 `sys.stdout` 换掉：

.. literalinclude:: /_src/practices/py2-encoding/say-hello-utf8.py
    :language: python
    :lines: 16-

.. code-block:: shell-session

    $ python2 say-hello-utf8.py | cat
    你好，世界！

看到没有，程序运行也正常了！

方法三：设置程序默认编码
------------------------

这是一个无脑大招，几乎可以应对大部分编码问题！

方法很简单，只需将入一下若干代码，重新设置程序的默认编码方式即可：

.. code-block:: python

    import sys
    reload(sys)
    sys.setdefaultencoding('UTF8')

下一步
======

.. include:: /_fragments/next-step-to-wechat-mp.rst

.. include:: /_fragments/wechat-reward.rst

.. include:: /_fragments/disqus.rst

.. comments
    comment something out below

