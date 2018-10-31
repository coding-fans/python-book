.. 更优雅地造测试数据
    FileName:   faker.rst
    Author:     Fasion Chan
    Created:    2018-10-31 18:12:32
    @contact:   fasionchan@gmail.com
    @version:   $Id$

    Description:

    Changelog:

.. meta::
    :keywords: python, faker, 测试数据, 姓名, 地址, 手机号, 邮箱, name, address, telephone, email

==================
更优雅地造测试数据
==================

开发系统时，经常需要一些伪数据用于测试。
举个例子，设计一个学生管理系统，测试注册功能，总需要一些用户信息吧。
我猜大部分人都会填：用户 ``aaaa`` ，密码 ``1111`` ，手机号码 ``1111`` ……感觉略无追求~

那么有没有办法造一些看上是真的数据呢？肯定是有的——人是活的嘛~

自己造很累，有没有不需要大脑的方法的？
还真有，这就是本文要介绍的一个 `Python` 模块—— `Faker <https://pypi.python.org/pypi/fake-factory>`_ 。

安装
====

其实，这节可以不必说， `Python` 装包无非就是 `pip` 嘛：

.. code-block:: shell-session

    $ pip install Faker

快速入手
========

生成数据前需要先初始化一个生成器，有两种方式可以完成：

#. 用 `faker.Factory.create()` ；
#. 用 `faker.Faker()` ；

.. code-block:: pycon

    >>> from faker import Factory
    >>> fake = Factory.create()

    >>> # OR
    >>> from faker import Faker
    >>> fake = Faker()

    >>> fake.name()
    'Lucy Cechtelar'

    >>> fake.address()
    '426 Jordy Lodge Cartwrightshire, SC 88120-6700'

    >>> fake.text()
    'Sint velit eveniet. Rerum atque repellat voluptatem quia rerum. Numquam excepturi beatae sint laudantium consequatur. Magni occaecati itaque sint et sit tempore. Nesciunt amet quidem. Iusto deleniti cum autem ad quia aperiam. A consectetur quos aliquam. In iste aliquid et aut similique suscipit. Consequatur qui quaerat iste minus hic expedita. Consequuntur error magni et laboriosam. Aut aspernatur voluptatem sit aliquam. Dolores voluptatum est. Aut molestias et maxime. Fugit autem facilis quos vero. Eius quibusdam possimus est. Ea quaerat et quisquam. Deleniti sunt quam. Adipisci consequatur id in occaecati. Et sint et. Ut ducimus quod nemo ab voluptatum.'

可以写一个循环批量生成：

.. code-block:: pycon

    >>> for _ in range(0, 10):
    ...     print(fake.name())
    ...
    Adaline Reichel
    Dr. Santa Prosacco DVM
    Noemy Vandervort V
    Lexi O'Conner
    Gracie Weber
    Roscoe Johns
    Emmett Lebsack
    Keegan Thiel
    Wellington Koelpin II
    Ms. Karley Kiehn V

看看自动化的威力！批量生成，每次都是随机的哦！

本地化
======

你可能会说，这个玩意儿太洋气了——生成一堆英文名字地址啥的有毛用？
确实，在计算机领域，英文有天生优势。

好在 `Faker` 还支持本地化，真是天地良心！
一起来看看怎么生成中文信息吧：

.. code-block:: pycon

    >>> from faker import Factory
    >>> fake = Factory.create('zh_CN')

    >>> for _ in range(0, 10):
    ...     print(fake.name())
    ...
    於涛
    万静
    孙秀荣
    丘辉
    方玉
    虞建国
    丘丽丽
    郭杨
    江欣
    狐龙

    >>> for _ in range(0, 10):
    ...     print(fake.address())
    ...
    杰市戚路d座 855521
    丽华市魏街e座 800775
    坤市莘路P座 376919
    秀云市温街s座 518607
    晨市季街Z座 931186
    丽市夹路N座 670627
    坤市漆街k座 968075
    瑞市於街z座 168689
    金凤市雍路E座 148292
    晨市黎路R座 916369

高级用法
========

功能扩展
--------

`Faker` 已经提供了足够丰富的信息生成，包括 **名字** 、 **手机号** 、 **邮箱地址** 、 **邮编** 等。
尽管如此，可能还是没有办法满足你的需求。
这时，你可以自己动手，丰衣足食。
下面，我们通过一个例子看看怎么扩展 `Faker` 的功能吧：

.. code-block:: python

    from faker import Faker
    fake = Faker()

    # first, import a similar Provider or use the default one
    from faker.providers import BaseProvider
    # create new provider class
    class MyProvider(BaseProvider):
        def foo(self):
            return 'bar'

    # then add new provider to faker instance
    fake.add_provider(MyProvider)

    fake.foo()

程序运行后，输出 ``bar`` 。

随机控制
--------

`Faker` 随机生成由 `random.Random` 驱动。
其中， `.random` 属性返回 `random.Random` 对象。
通过对该对象的操作，可以实现自定义的行为。

.. code-block:: python

    from faker import Faker
    fake = Faker()
    fake.random
    fake.random.getstate()

那么，可以实现什么自定义呢？
举个例子，我们可以设置 `seed` 。
`seed` 在随机数生成逻辑中什么作用，估计大家都清楚。
比如，通过给定 `seed` 可以控制每次生成的内容都是一样的：

.. code-block:: pycon

    >>> from faker import Faker
    >>> fake = Faker()
    >>> faker.random.seed(4321)
    >>> print(fake.name())
    Margaret Boehm

还有等价写法哦：

.. code-block:: pycon

    >>> from faker import Faker
    >>> fake = Faker()
    >>> fake.seed(4321)
    >>> print(fake.name())
    Margaret Boehm

注意到，不同的两次运行，只要 `seed` 一样，生成出来的信息就是一样的。

命令行生成
----------

有时想在 `shell` 或者其他程序中生成一些伪数据，是不是一定要写一个 `Python` 脚本呢？
当然不是—— `Faker` 提供了一个命令行工具，应该可以应对大部分场景了：

.. code-block:: shell-session

    $ faker address
    968 Bahringer Garden Apt. 722Kristinaland, NJ 09890

    $ faker -l de_DE address
    Samira-Niemeier-Allee 5694812 Biedenkopf

    $ faker profile ssn,birthdate
    {'ssn': u'628-10-1085', 'birthdate': '2008-03-29'}

    $ faker -r=3 -s=";" name
    Willam Kertzmann;
    Josiah Maggio;
    Gayla Schmitt;

最后，可以通过 `-h` 选项查看使用帮助：

.. code-block:: shell-session

    $ faker -h
    usage: faker [-h] [--version] [-o output] [-l LOCALE] [-r REPEAT] [-s SEP]
                 [-i [INCLUDE [INCLUDE ...]]]
                 [fake] [fake argument [fake argument ...]]

下一步
======

.. include:: /_fragments/next-step-to-wechat-mp.rst

.. include:: /_fragments/wechat-reward.rst

.. include:: /_fragments/disqus.rst

.. comments
    comment something out below

