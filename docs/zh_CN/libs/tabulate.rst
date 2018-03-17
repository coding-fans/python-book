.. tabulate
    FileName:   tabulate.rst
    Author:     Fasion Chan
    Created:    2018-03-14 20:40:35
    @contact:   fasionchan@gmail.com
    @version:   $Id$

    Description:

    Changelog:

.. meta::
    :description lang=zh:
        用过 MySQL 的童鞋一定对那个非常好看的字符表格印象深刻吧！
        在 Python 中，使用 tabulate 库，可轻松实现一模一样的字符表格。
        from tabulate import tabulate
        print(tabulate(table_data, headers=table_header, tablefmt='grid'))
    :keywords: python, tabulate, 输出表格, 字符表格, 格式化表格式数据, MySQL表格输出

========
tabulate
========

用过 ``MySQL`` 的童鞋一定对那个非常好看的字符表格印象深刻吧！

在 `Python` 中，使用 `tabulate <https://pypi.python.org/pypi/tabulate>`_ 库，可轻松实现一模一样的字符表格。

快速上手
========

废话不多说，先来看看效果：

.. code-block:: pycon

	>>> from tabulate import tabulate

	>>> table_header = ['Name', 'Chinese', 'Math', 'English']
	>>> table_data = [
	...     ('Tom', '90', '80', '85'),
	...     ('Jim', '70', '90', '80'),
	...     ('Lucy', '90', '70', '90'),
	... ]

	>>> print(tabulate(table_data, headers=table_header, tablefmt='grid'))
	+--------+-----------+--------+-----------+
	| Name   |   Chinese |   Math |   English |
	+========+===========+========+===========+
	| Tom    |        90 |     80 |        85 |
	+--------+-----------+--------+-----------+
	| Jim    |        70 |     90 |        80 |
	+--------+-----------+--------+-----------+
	| Lucy   |        90 |     70 |        90 |
	+--------+-----------+--------+-----------+

上述代码，先从 `tabulate` 库导入同名工具函数；
接着，定义一个用于演示的数据表格，包括表头和表数据；
最后，用 ``tabulate`` 函数格式化表格，传参包括表数据，表头以及表格样式。

看到没有，引入 ``tabulate`` 函数后，只需要一行代码即可完成表格输出！

回过头来看看如何安装 `tabulate` 。你可能已经猜到了：

.. code-block:: shell-session

    $ pip install tabulate

是的，就是这么简单！

表格样式
========

`tabulate` 提供多种表格输出风格，列举如下：

plain
-----

.. code-block:: pycon

	>>> print(tabulate(table_data, headers=table_header, tablefmt='plain'))
	Name      Chinese    Math    English
	Tom            90      80         85
	Jim            70      90         80
	Lucy           90      70         90

simple
------

.. code-block:: pycon

	>>> print(tabulate(table_data, headers=table_header, tablefmt='simple'))
	Name      Chinese    Math    English
	------  ---------  ------  ---------
	Tom            90      80         85
	Jim            70      90         80
	Lucy           90      70         90

grid
----

.. code-block:: pycon

	>>> print(tabulate(table_data, headers=table_header, tablefmt='grid'))
	+--------+-----------+--------+-----------+
	| Name   |   Chinese |   Math |   English |
	+========+===========+========+===========+
	| Tom    |        90 |     80 |        85 |
	+--------+-----------+--------+-----------+
	| Jim    |        70 |     90 |        80 |
	+--------+-----------+--------+-----------+
	| Lucy   |        90 |     70 |        90 |
	+--------+-----------+--------+-----------+

fancy_grid
----------

.. code-block:: pycon

	>>> print(tabulate(table_data, headers=table_header, tablefmt='fancy_grid'))
	╒════════╤═══════════╤════════╤═══════════╕
	│ Name   │   Chinese │   Math │   English │
	╞════════╪═══════════╪════════╪═══════════╡
	│ Tom    │        90 │     80 │        85 │
	├────────┼───────────┼────────┼───────────┤
	│ Jim    │        70 │     90 │        80 │
	├────────┼───────────┼────────┼───────────┤
	│ Lucy   │        90 │     70 │        90 │
	╘════════╧═══════════╧════════╧═══════════╛

pipe
----

.. code-block:: pycon

	>>> print(tabulate(table_data, headers=table_header, tablefmt='pipe'))
	| Name   |   Chinese |   Math |   English |
	|:-------|----------:|-------:|----------:|
	| Tom    |        90 |     80 |        85 |
	| Jim    |        70 |     90 |        80 |
	| Lucy   |        90 |     70 |        90 |

orgtlb
------

.. code-block:: pycon

	>>> print(tabulate(table_data, headers=table_header, tablefmt='orgtbl'))
	| Name   |   Chinese |   Math |   English |
	|--------+-----------+--------+-----------|
	| Tom    |        90 |     80 |        85 |
	| Jim    |        70 |     90 |        80 |
	| Lucy   |        90 |     70 |        90 |

jira
----

.. code-block:: pycon

	>>> print(tabulate(table_data, headers=table_header, tablefmt='jira'))
	|| Name   ||   Chinese ||   Math ||   English ||
	| Tom    |        90 |     80 |        85 |
	| Jim    |        70 |     90 |        80 |
	| Lucy   |        90 |     70 |        90 |

presto
------

.. code-block:: pycon

	>>> print(tabulate(table_data, headers=table_header, tablefmt='presto'))
	 Name   |   Chinese |   Math |   English
	--------+-----------+--------+-----------
	 Tom    |        90 |     80 |        85
	 Jim    |        70 |     90 |        80
	 Lucy   |        90 |     70 |        90

psql
----

.. code-block:: pycon

	>>> print(tabulate(table_data, headers=table_header, tablefmt='psql'))
	+--------+-----------+--------+-----------+
	| Name   |   Chinese |   Math |   English |
	|--------+-----------+--------+-----------|
	| Tom    |        90 |     80 |        85 |
	| Jim    |        70 |     90 |        80 |
	| Lucy   |        90 |     70 |        90 |
	+--------+-----------+--------+-----------+

rst
---

.. code-block:: pycon

	>>> print(tabulate(table_data, headers=table_header, tablefmt='rst'))
	======  =========  ======  =========
	Name      Chinese    Math    English
	======  =========  ======  =========
	Tom            90      80         85
	Jim            70      90         80
	Lucy           90      70         90
	======  =========  ======  =========

html
----

.. code-block:: pycon

    >>> print(tabulate(table_data, headers=table_header, tablefmt='html'))
    <table>
    <thead>
    <tr><th>Name  </th><th style="text-align: right;">  Chinese</th><th style="text-align: right;">  Math</th><th style="text-align: right;">  English</th></tr>
    </thead>
    <tbody>
    <tr><td>Tom   </td><td style="text-align: right;">       90</td><td style="text-align: right;">    80</td><td style="text-align: right;">       85</td></tr>
    <tr><td>Jim   </td><td style="text-align: right;">       70</td><td style="text-align: right;">    90</td><td style="text-align: right;">       80</td></tr>
    <tr><td>Lucy  </td><td style="text-align: right;">       90</td><td style="text-align: right;">    70</td><td style="text-align: right;">       90</td></tr>
    </tbody>
    </table>

注意到， ``tabulate`` 函数也可以用来生成 ``html`` 表格定义代码。
此外，还支持 ``mediawiki`` 、 ``moinmoin`` 、 ``youtrack`` 、 ``latex`` 、 ``latex_raw`` 、 ``latex__booktabs`` 、 ``textile`` 表格生成。

下一步
======

.. include:: /_fragments/next-step-to-wechat-mp.rst

.. include:: /_fragments/wechat-reward.rst
