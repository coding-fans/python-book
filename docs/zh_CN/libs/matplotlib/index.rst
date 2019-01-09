.. matplotlib
    FileName:   index.rst
    Author:     Fasion Chan
    Created:    2019-01-03 18:36:43
    @contact:   fasionchan@gmail.com
    @version:   $Id$

    Description:

    Changelog:

.. meta::
    :description lang=zh:
        matplotlib是一个用于科学计算绘图的Python包，功能非常强大，堪比Matlab！
        饼状图应该是最简单的统计图表了，用以介绍matplotlib画图方式最为合适。
        让matplotlib支持中文的方式有不少，接下来介绍一种最简单的。
    :keywords: python, matplotlib, matlab, pie, font, 中文, 统计图表, 科学计算

==========
matplotlib
==========

`matplotlib`_ 是一个用于 **科学计算绘图** 的 `Python` 包，功能非常强大，堪比 `Matlab`_ ！
开始前，先通过几张图来感受一下：

.. figure:: /_images/libs/matplotlib/index/93498df23549c42e72dcd5361dce6f7b.png


快速开始
========

饼状图应该是最简单的统计图表了，用以介绍 `matplotlib`_ 画图方式最为合适。
数据准备就绪，生成饼状图只需若干行代码：

.. literalinclude:: /_src/libs/matplotlib/pie.py
    :caption:
    :name: libs/matplotlib/pie.py
    :language: python
    :lines: 19-
    :linenos:

第 *4-5* 行，为待渲染数据，包括 **数值** 以及 **标签** ；
第 *7* 行，定义渲染 **颜色** ；
第 *9-14* 行，配置饼图，包括数值、标签、颜色以及百分比展示；
第 *16* 行，为图表追加 **标题** ；
第 *18* 行，将图表展示出来。

运行程序后，画出的图表效果如下：

.. figure:: /_images/libs/matplotlib/index/ca76641457d181dd6713f2f5d6681164.png
    :width: 640px

字体
====

在编程世界，中文一直是个麻烦事。
不折腾一番， `matplotlib`_ 是不能渲染中文文本的。

让 `matplotlib`_ **支持中文** 的方式有不少，接下来介绍一种最简单的：
准备好字体文件，为文本定义 `FontProperties`_ 并设置。
除了指定 **字体** ， `FontProperties`_ 还支持 **字号** 、 **粗细** 、 **斜体** 、 **下划线** 等属性设置。

.. literalinclude:: /_src/libs/matplotlib/font.py
    :caption:
    :name: libs/matplotlib/font.py
    :language: python
    :lines: 19-
    :linenos:

程序第 `11-15` 行加载字体文件，并设置字号；
第 `17-18` 行在第一个标签字体基础上设置新字号，作为标题字体，
第 `33-34` 行为 *4* 个标签分别设置字体；
第 `36` 行指定标题，同时设置标题字体。

运行程序后，画出的图表效果如下：

.. figure:: /_images/libs/matplotlib/index/47e3e92e52e71feb5b01afe83a5b4135.png
    :width: 640px

.. note::

    `Github`_ 上有个项目提供一些字体文件，以供测试： `dolbydu/font <https://github.com/dolbydu/font>`_ 。

保存图片
========

将图表保存成文件，只需调用 `savefig` 方法。保存为 `PNG` 图片：

.. code-block:: python

    plt.savefig('foo.png')

文件格式由文件后缀名决定，另存为 `PDF` 文件：

.. code-block:: python

    plt.savefig('foo.pdf')

如果仅需获取保存文件内容，则可借助 `BytesIO` ：

.. code-block:: python

    import io

    bio = io.BytesIO()
    plt.savefig(bio, format='png')

    bio.seek(0)
    content = bio.read()

下一步
======

.. toctree::
    :titlesonly:

    疑难杂症 <issues>

参考文献
========

#. `Matplotlib Pie chart - Python Tutorials <https://pythonspot.com/matplotlib-pie-chart/>`_

.. include:: /_fragments/next-step-to-wechat-mp.rst

.. include:: /_fragments/wechat-reward.rst

.. include:: /_fragments/disqus.rst

.. _FontProperties: https://matplotlib.org/api/font_manager_api.html#matplotlib.font_manager.FontProperties
.. _Github: https://github.com
.. _Matlab: https://www.mathworks.com/products/matlab.html
.. _matplotlib: https://matplotlib.org

.. comments
    comment something out below

