.. openpyxl
    FileName:   openpyxl.rst
    Author:     Fasion Chan
    Created:    2018-10-15 20:44:41
    @contact:   fasionchan@gmail.com
    @version:   $Id$

    Description:

    Changelog:

.. meta::
    :keywords: python, excel, openpyxl

========
openpyxl
========

`Python` 可以读写 `Excel` 表格吗？

那当然。 `Python` 下有很多类库可以做到， `openpyxl`_ 就是其中的佼佼者。

`openpyxl`_ 的 **设计非常漂亮** ，你一定会喜欢它！不信请往下看：

工作簿
======

开始 `openpyxl`_ 前，无需提前建好工作簿( `Workbook` )。
只需导入 `Workbook` 类，便可开始在内存中创建并操作工作簿：

.. code-block:: pycon

    >>> from openpyxl import Workbook
    >>> wb = Workbook()

新建的工作簿默认预先建好一个工作表，通过 `active` 属性获取：

.. code-block:: pycon

    >>> ws = wb.active

.. note::

    如果工作簿包含多个工作表，该属性将返回第一个。

通过 `create_sheet` 方法，可以创建新的工作表。
创建可以是在后面追加：

.. code-block:: pycon

    >>> ws1 = wb.create_sheet('Mysheet')

或者，在前面插入：

.. code-block:: pycon

    >>> ws1 = wb.create_sheet('Mysheet', 0)

未指定表格名将自动生成，序列形如： `Sheet` 、 `Sheet1` 、 `Sheet2` ，以此类推。
当然了，你觉得不合适可以进行修改：

.. code-block:: pycon

    >>> ws.title = 'New Title'

工作表标题标签背景颜色默认是白色。
用一个 `RGB` 颜色代码设置 `sheet_properties.tabColor` 属性即可修改：

.. code-block:: pycon

    ws.sheet_properties.tabColor = "1072BA"

一旦你给工作表命名，便可以通过该名字来定位：

.. code-block:: pycon

    >>> ws3 = wb["New Title"]

通过 `sheetnames` 方法，可以取出所有工作表表名：

.. code-block:: pycon

    >>> print(wb.sheetnames)
    ['Sheet2', 'New Title', 'Sheet1']

当然了，遍历所有工作表，直接 `for-in` 更为优雅：

.. code-block:: pycon

    >>> for sheet in wb:
    ...     print(sheet.title)

使用 `copy_worksheet` 方法，可在工作簿内拷贝工作表：

.. code-block:: pycon

    >>> source = wb.active
    >>> target = wb.copy_worksheet(source)

数据处理
========

单单元格
--------

操作工作表，从修改单元格内容开始。单元格可以通过工作表键直接访问：

.. code-block:: pycon

    >>> c = ws['A4']

这个语句将返回 `A4` 单元格，或者在单元格不存在时创建它。可以直接赋值：

.. code-block:: pycon

    >>> ws['A4'] = 10

另一种方式是使用 `cell` 方法访问单元格，给定行列：

.. code-block:: pycon

    >>> d = ws.cell(row=4, column=2, value=10)

.. note::

    工作表创建后，不包含任何单元格，单元格在第一次被访问时自动创建。

多单元格
--------

连续多个单元格可以通过切片获得：

.. code-block:: pycon

    >>> cell_range = ws['A1':'C2']

以行或类为单位也可以：

.. code-block:: pycon

    >>> colC = ws['C']
    >>> col_range = ws['C:D']
    >>> row10 = ws[10]
    >>> row_range = ws[5:10]

使用 `iter_rows` 方法也可以：

.. code-block:: pycon

    >>> for row in ws.iter_rows(min_row=1, max_col=3, max_row=2):
    ...    for cell in row:
    ...        print(cell)
    <Cell Sheet1.A1>
    <Cell Sheet1.B1>
    <Cell Sheet1.C1>
    <Cell Sheet1.A2>
    <Cell Sheet1.B2>
    <Cell Sheet1.C2>

如需遍历表格所有行或列，可以使用相关属性。使用 `rows` 属性遍历所有行：

.. code-block:: pycon

    >>> ws = wb.active
    >>> ws['C9'] = 'hello world'
    >>> tuple(ws.rows)
    ((<Cell Sheet.A1>, <Cell Sheet.B1>, <Cell Sheet.C1>),
    (<Cell Sheet.A2>, <Cell Sheet.B2>, <Cell Sheet.C2>),
    (<Cell Sheet.A3>, <Cell Sheet.B3>, <Cell Sheet.C3>),
    (<Cell Sheet.A4>, <Cell Sheet.B4>, <Cell Sheet.C4>),
    (<Cell Sheet.A5>, <Cell Sheet.B5>, <Cell Sheet.C5>),
    (<Cell Sheet.A6>, <Cell Sheet.B6>, <Cell Sheet.C6>),
    (<Cell Sheet.A7>, <Cell Sheet.B7>, <Cell Sheet.C7>),
    (<Cell Sheet.A8>, <Cell Sheet.B8>, <Cell Sheet.C8>),
    (<Cell Sheet.A9>, <Cell Sheet.B9>, <Cell Sheet.C9>))

使用 `columns` 属性遍历所有列：

.. code-block:: pycon

    >>> tuple(ws.columns)
    ((<Cell Sheet.A1>,
    <Cell Sheet.A2>,
    <Cell Sheet.A3>,
    <Cell Sheet.A4>,
    <Cell Sheet.A5>,
    <Cell Sheet.A6>,
    ...
    <Cell Sheet.B7>,
    <Cell Sheet.B8>,
    <Cell Sheet.B9>),
    (<Cell Sheet.C1>,
    <Cell Sheet.C2>,
    <Cell Sheet.C3>,
    <Cell Sheet.C4>,
    <Cell Sheet.C5>,
    <Cell Sheet.C6>,
    <Cell Sheet.C7>,
    <Cell Sheet.C8>,
    <Cell Sheet.C9>))

数据存储
========

`Excel` 表格通过单元格存储数据，直接赋值即可：

.. code-block:: pycon

    >>> c.value = 'hello, world'
    >>> print(c.value)
    'hello, world'

    >>> d.value = 3.14
    >>> print(d.value)
    3.14

与此同时，还可以附加类型以及格式化信息：

.. code-block:: pycon

    >>> wb = Workbook(guess_types=True)
    >>> c.value = '12%'
    >>> print(c.value)
    0.12

    >>> import datetime
    >>> d.value = datetime.datetime.now()
    >>> print d.value
    datetime.datetime(2010, 9, 10, 22, 25, 18)

    >>> c.value = '31.50'
    >>> print(c.value)
    31.5


保存至文件
----------

最保险的保存方式是调用 `save` 方法保存到指定文件：

.. code-block:: pycon

    >>> wb = Workbook()
    >>> wb.save('balances.xlsx')

.. warning::

    这个操作将覆盖已存在的文件，没有任何提示！

借助 `template` 属性，可以将工作表保存成文档：

.. code-block:: pycon

    >>> wb = load_workbook('document.xlsx')
    >>> wb.template = True
    >>> wb.save('document_template.xltx')

或者保存成普通文档：

.. code-block:: pycon

    >>> wb = load_workbook('document_template.xltx')
    >>> wb.template = False
    >>> wb.save('document.xlsx', as_template=False)


保存至流
--------

在 `Flask` 、 `Django` 等 `Web` 应用，可能需要将文件保存到流( `stream` )。
借助一个临时文件( `NamedTemporaryFile` )可以轻松解决：

.. code-block:: pycon

    >>> from tempfile import NamedTemporaryFile
    >>> from openpyxl import Workbook
    >>> wb = Workbook()
    >>> with NamedTemporaryFile() as tmp:
    ...     wb.save(tmp.name)
    ...     tmp.seek(0)
    ...     stream = tmp.read()

从文件加载
==========

导入 `openpyxl.load_workbook` 函数来加载已存在的工作簿：

.. code-block:: pycon

    >>> from openpyxl import load_workbook
    >>> wb2 = load_workbook('test.xlsx')
    >>> print wb2.sheetnames
    ['Sheet2', 'New Title', 'Sheet1']

下一步
======

.. include:: /_fragments/next-step-to-wechat-mp.rst

.. include:: /_fragments/wechat-reward.rst

.. include:: /_fragments/disqus.rst

.. _openpyxl: https://openpyxl.readthedocs.io/en/stable/

.. comments
    comment something out below

