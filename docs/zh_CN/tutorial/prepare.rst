..
    Author: huangxiaoyan
    Created time: 2020-02-29 11:18:33
    Last Modified by: fasion
    Last Modified time: 2020-03-21 23:18:43

====================
搭建 Python 编程环境
====================

*Python* 是一种解释型、面向对象、动态数据类型的高级程序设计语言。
语法简单易学，不管是用来专业开发，还是业余辅助办公，都是不二之选。
本教程将结合实际应用场景，提供丰富的例子，一步步教你快速掌握 *Python*。

开始学习 *Python* 编程前，需要先准备 *Python* 运行环境。

*Python* 编程环境搭建步骤，因操作系统类型而异。
目前，市面上主流操作系统有 :ref:`prepare-windows` ，以及 `Linux`_ 、 *macOS* 等类 :ref:`prepare-unix` 系统，编程环境搭建步骤分别如下：

- :ref:`prepare-windows`
- :ref:`prepare-unix`

.. _prepare-windows:

Windows
=======

如果你使用的是 *Windows* 系统，就需要手动进行安装。
下面以 *Windows 10* 系统为例，介绍如何安装并运行 *Python* 。

下载 Python
-----------

首先，进入 *Python* 官网( `www.python.org`_ )，下载最新版本。如果需要下载其他的 *Python* 版本，也可以在下载页面找到对应的版本：

.. figure:: /_images/tutorial/prepare/8333a0438108a6918bb019f59915922c.png
    :width: 441px

选择对应版本后，可以找到这些安装程序，请根据系统位数选择：

.. figure:: /_images/tutorial/prepare/cdfc0bddc3e38e96ce9b509061c162c8.png
    :width: 460px

本文以 *Python 3.8.1* 为例，演示 *Python* 安装方法。

安装 Python
-----------

下载后的 *Python 3.8.1* 版本是一个 *exe* 文件，即可执行文件，双击该文件进行安装：

.. figure:: /_images/tutorial/prepare/bc058ec0ac3b9c727de6aec8e8f40048.png
    :width: 600px

点击 *Install Now* ，选择要安装的组件，默认即可:

.. figure:: /_images/tutorial/prepare/183c7f22507364172b0c3dfe4bc630cb.png
    :width: 600px

点击 *Next*，出现下图:

.. figure:: /_images/tutorial/prepare/328f3d36b38281c4e8610158c0ab531a.png
    :width: 600px

在此勾选 *Add Python to environment variables*，意为将 *Python* 加入环境变量：

.. figure:: /_images/tutorial/prepare/845b26786be67369999be4da7c63e8fa.png
    :width: 600px

点击 *Install*，开始安装。

运行 Python
-----------

现在，让我们来验证下，*Python* 是否安装成功了。

IDLE
++++

我们可以使用 *Python* 的 *IDLE* 工具来执行代码。在 *Windows* 搜索框输入 *idle*：

.. figure:: /_images/tutorial/prepare/25e827b9d57fd969aff754c5eff991c7.png
    :width: 600px

打开 *IDLE* 工具，可以看到如下界面：

.. figure:: /_images/tutorial/prepare/bb0399070c7d32c0728a82160bea01ee.png
    :width: 600px

三个大于号组成输入提示符 ``>>>``，提示我们输入需要执行的 *Python* 代码。

现在，让 *Python* 执行什么任务好呢？不如先让它在屏幕上打印一句话吧！
输入 ``print('Hello, world!')`` ，然后按回车：

.. figure:: /_images/tutorial/prepare/9c993ff30d24652b983f83a8ba98fcec.png
    :width: 600px

看到没， *Python* 在屏幕上输出了 ``Hello, world!`` ！

你或许还心存疑虑，然而此刻你只需知道 *print* 是一个将内容输出到屏幕的函数，单引号包括的是待输出内容即可。
至于其他的，我们接着慢慢学习。

CMD
+++

除了 *IDLE* 工具外，也可以使用 *Windows* 的命令行工具来启动 *Python* 程序。

同样，*Windows* 搜索框输入 *cmd*：

.. figure:: /_images/tutorial/prepare/f07028520b90eb758cae80c85c0ed4ea.png
    :width: 600px

由此可以打开 *Windows* 命令行工具：

.. figure:: /_images/tutorial/prepare/1279dc29cb3fb67995797b1a815c14e7.png
    :width: 600px

首先，输入 *python* 并按回车，即可启动 *Python* 终端。
如果看到以下界面，说明 *Windows* 找到了这个程序：

.. figure:: /_images/tutorial/prepare/359b20925aeaec421620f09d40739d8c.png
    :width: 600px

还记得在安装时，我们勾选了将 *Python* 加入到环境变量吗？正是这一步，让 *Windows* 能够识别 *Python* 程序。

我们同样让 *Python* 输出一句话。输入 ``print('Hello, world!')``，然后按回车：

.. figure:: /_images/tutorial/prepare/2b61abc3cbfe066babe267c1792c48fa.png
    :width: 600px

可以看到，屏幕同样输出了 ``Hello, world!``。

至此，*Python* 环境搭建完毕，可以愉快地开始学习了！

.. _prepare-unix:

Unix
====

如果你使用的是 *Linux* 和 *macOS* 等类 *Unix* 系统，事情就简单了。
类 *Unix* 系统一般都内置了 *Python* 环境，打开终端工具，即可使用。

以 *MacOS* 为例，先找到系统终端程序，它一般是这个样子的：

.. figure:: /_images/tutorial/prepare/103edcde70f4483d67d4bb57f4a7cfb8.png

打开终端，将看到以下界面：

.. figure:: /_images/tutorial/prepare/987c88e5e6860bc61280df7035adb73e.png

输入 *python*，然后按回车，启动 *Python* 解析器：

.. figure:: /_images/tutorial/prepare/fcfab7c8303c418d371d288f66609ec6.png

三个大于号组成输入提示符 ``>>>`` ，提示我们输入需要执行的 *Python* 代码。

现在，让 *Python* 执行什么任务好呢？不如先让它在屏幕上打印一句话吧！
输入 ``print('Hello, world!')`` ，然后按回车：

.. figure:: /_images/tutorial/prepare/f9a8891083f963159dd1278164721add.png

看到没， *Python* 在屏幕上输出了 ``Hello, world!`` ！

你或许还心存疑虑，然而此刻你只需知道 *print* 是一个将内容输出到屏幕的函数，单引号包括的是待输出内容即可。
至于其他的，我们接着慢慢学习。

附录
====

.. include:: /_fragments/appendix.rst

.. include:: /_fragments/disqus.rst

.. _Linux: https://linux.fasionchan.com/zh_CN/latest/index.html
.. _www.python.org: https://www.python.org/
