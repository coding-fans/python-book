.. html-table
    FileName:   html-table.rst
    Author:     Fasion Chan
    Created:    2019-04-09 15:38:19
    @contact:   fasionchan@gmail.com
    @version:   $Id$

    Description:

    Changelog:

.. meta::
    :keywords: python, html, table, generate, 生成, rowspan, colspan, css, 合并单元格, html-table

==========
html-table
==========

在 **邮件报表** 之类的开发任务中，需要生成 `HTML` 表格。

使用 `Python` 生成 `HTML` 表格基本没啥难度， `for` 循环遍历一遍数据并输出标签即可。
如果需要实现合并单元格，或者按需调整表格样式，就比较麻烦了。

这时，可以试试本文的主角—— `html-table`_ 包，借助它可生成各种样式的 `HTML` 表格。
接下来，以一个简单的例子演示 `html-table` 的常用用法：

.. figure:: /_images/libs/html-table/997ad67a7f305a39e5a77e3bf86c7798.png
    :width: 366px

开始之前，须通过 `pip` 安装 `html-table`_ 包：

.. code-block:: shell-session

    $ python -m pip install html-table

安装完毕后，即可导入 `HTMLTable` 类：

.. literalinclude:: /_src/libs/html-table/fruit-output.py
    :language: python
    :lines: 16-18

创建一个新表格，标题为 *果园收成表* ：

.. literalinclude:: /_src/libs/html-table/fruit-output.py
    :language: python
    :lines: 20-21

附上表头：

.. literalinclude:: /_src/libs/html-table/fruit-output.py
    :language: python
    :lines: 23-27

注意到，表头分为两行，有些单元格需要合并，被合并的单元格需要留空占位。

合并单元格设置：

.. literalinclude:: /_src/libs/html-table/fruit-output.py
    :language: python
    :lines: 29-32

*table[0]* 取出第一行，即第一个 *<tr>* 标签；
*table[0][0]* 取出第一个单元格，对应 **名称** ；
*table[0][0].attr* 则是其标签 *<th>* 的属性。
该单元格合并下方一个单元格，需要将标签属性 *rowspan* 设置为 *2* 。

接着，加入数据，方法与表头类似，总共有 *3* 行：

.. literalinclude:: /_src/libs/html-table/fruit-output.py
    :language: python
    :lines: 34-39

至此，数据准备完毕，可以着手调整样式。先设置表格标题样式：

.. literalinclude:: /_src/libs/html-table/fruit-output.py
    :language: python
    :lines: 41-44

设置 *<table>* 标签的样式：

.. literalinclude:: /_src/libs/html-table/fruit-output.py
    :language: python
    :lines: 46-53

以上 `CSS` 样式设置在 `<table>` 标签上，作用于整个表格，影响表格边框、字体大小等。
注意到，下面会覆盖部分单元格(如表头单元格)的字体大小。

接着，设置每个单元格的样式，主要是规定边框样式：

.. literalinclude:: /_src/libs/html-table/fruit-output.py
    :language: python
    :lines: 55-62

接着，设置表头单元格样式，规定颜色、字体大小、以及填充大小：

.. literalinclude:: /_src/libs/html-table/fruit-output.py
    :language: python
    :lines: 64-73

`set_header_row_style` 将样式设置到表头两个 `<tr>` 标签上；
`set_header_cell_style` 则将样式设置到每个 *<th>* 标签上。
应该尽量将颜色等样式设置到 *<tr>* 标签上，而不是 *<th>* 标签上，以精简生成的 *HTML* 。

将次级表头字体大小调小，不在赘述：

.. literalinclude:: /_src/libs/html-table/fruit-output.py
    :language: python
    :lines: 75-79

遍历每个数据行，如果第 *2* 个单元格值小于 *0* ，设置样式标红背景颜色：

.. literalinclude:: /_src/libs/html-table/fruit-output.py
    :language: python
    :lines: 81-86

最后，生成 `HTML` 文本：

.. literalinclude:: /_src/libs/html-table/fruit-output.py
    :language: python
    :lines: 88-89

下一步
======

.. include:: /_fragments/next-step-to-wechat-mp.rst

.. include:: /_fragments/wechat-reward.rst

.. include:: /_fragments/disqus.rst

.. _html-table: https://github.com/fasionchan/py-html-table

.. comments
    comment something out below

