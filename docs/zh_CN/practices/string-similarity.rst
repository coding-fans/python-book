.. Python计算字符串相似度
    FileName:   string-similarity.rst
    Author:     Fasion Chan
    Created:    2018-12-10 17:16:50
    @contact:   fasionchan@gmail.com
    @version:   $Id$

    Description:

    Changelog:

.. meta::
    :description lang=zh:
        基于difflib.SequenceMatcher类，我们可以实现一个用于计算字符串相似度的函数。
        ratio方法返回一个系数，衡量两个字符串的相识度，取值在0-1之间。
    :keywords: python, string similarity, 字符串相似度, difflib

======================
Python计算字符串相似度
======================

背景
====

笔者最近有个任务需要从多个系统取出工单信息进行处理，
但是工单只有一个标题可以关联，而且还不是严格相等的。
例如：

- 易查通日常升级的发布请示
- 【易查通】易查通系统日常升级

这种判断比较棘手，只能利用 **字符串相似度** 进行衡量：

.. code-block:: python

    if similarity('易查通日常升级的发布请示', '【易查通】易查通系统日常升级') > 0.5:
        print('哥俩是同个工单')

那么， `Python` 有现成的类库可衡量字符串相似度么？

difflib
=======

基于 `difflib.SequenceMatcher`_ 类，我们可以实现一个用于计算字符串相似度的函数：

.. code-block:: python

    from difflib import SequenceMatcher

    def similarity(a, b):
        return SequenceMatcher(None, a, b).ratio()

`ratio` 方法返回一个系数，衡量两个字符串的相识度，取值在 `0-1` 之间。

如果两个字符串完全相同，则系数为 `1.0` ：

.. code-block:: pycon

    >>> similarity('fasionchan', 'fasionchan')
    1.0

如果两个字符串完全没有任何相同之处，则系数为 `0.0` ：

.. code-block:: pycon

    >>> similarity('fasionchan', '')
    0.0
    >>> similarity('aaaaaaaa', 'bbbbbbbb')
    0.0

其他情况则介于 `0` 与 `1` 之间，越接近 `1` 越相似：

.. code-block:: pycon

    >>> similarity('apple', 'banana')
    0.18181818181818182
    >>> similarity('易查通日常升级的发布请示', '【易查通】易查通系统日常升级')
    0.5384615384615384

下一步
======

.. include:: /_fragments/next-step-to-wechat-mp.rst

.. include:: /_fragments/wechat-reward.rst

.. include:: /_fragments/disqus.rst

.. _difflib.SequenceMatcher: https://docs.python.org/2/library/difflib.html#difflib.SequenceMatcher

.. comments
    comment something out below

