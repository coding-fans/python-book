..
    Author: fasion
    Created time: 2019-10-17 19:14:01
    Last Modified by: fasion
    Last Modified time: 2019-10-17 11:10:35

============================
从创建到销毁，对象的生命周期
============================

对象的创建
==========

.. code-block:: c

    PyObject* f = PyObject_New(PyObject, &PyFloat_Type)


引用计数
========

`C/C++` 赋予程序员极大的自由，可以任意申请内存，并按自己的意图灵活管理。
然而，权利的另一面则对应着 **责任** ，一旦内存不再使用，程序员必须将其释放。
这给程序员带来极大的 **工作负担** ，并导致大量问题： **内存泄露** 、 **野指针** 、 **越界访问** 等。

许多后来兴起的开发语言，如 `Java` 、 `Golang` 等，选择 **由语言本身负责内存的管理** 。
**垃圾回收机制** 的引入，程序员摆脱了内存管理的噩梦，可以更专注于业务逻辑。
于此同时，开发人员也失去了灵活使用内存的机会，也牺牲了一定的执行效率。

随着垃圾回收机制日益完善，可在大部分对性能要求不苛刻的场景中引入，利大于弊。
`Python` 也采用垃圾回收机制，代替程序员进行繁重的内存管理，**提升开发效率** 的同时，降低 `bug` 发生的几率。

`Python` 垃圾回收机制的关键是对象的 **引用计数** ，它决定了一个对象的生死。
我们知道每个 `Python` 对象都有一个 `ob_refcnt` 字段，记录着对象当前的引用计数。
当对象被其他地方引用时， `ob_refcnt` 加一；
当引用解除时， `ob_refcnt` 减一。
当引用计数为零，说明对象已经没有任何引用了，这时便可将其回收。

`Python` 对象创建后，引用计数设为 *1* ：

.. code-block:: pycon

    >>> a = 3.14
    >>> sys.getrefcount(a)
    2

咦？这里引用计数为啥是 *2* 呢？
对象作为函数参数传递，需要将引用计数加一，避免对象被提前销毁；函数返回时，再将引用计数减一。
因此，例子中 `getrefcount` 函数看到的对象引用计数为 *2* 。

接着，变量赋值让对象多了一个引用，这很好理解：

.. code-block:: pycon

    >>> b = a
    >>> sys.getrefcount(a)
    3

将对象放在容器对象中，引用计数也增加了，符合预期：

.. code-block:: pycon

    >>> l = [a]
    >>> l
    [3.14]
    >>> sys.getrefcount(a)
    4

我们将 `b` 变量删除，引用计数减少了：

.. code-block:: pycon

    >>> del b
    >>> sys.getrefcount(a)
    3

接着，将列表清空，引用计数进一步下降：

.. code-block:: pycon

    >>> l.clear()
    >>> sys.getrefcount(a)
    2

最后，将变量 *a* 删除后，引用计数降为 *0* ，便不复存在了：

.. code-block:: pycon

    >>> del b

在 `Python` 中，很多场景都涉及引用计数的调整，例如：

- 容器操作；
- 变量赋值(本质上是容器操作)；
- 函数参数传递(本质上是变量赋值)；
- 属性操作(本质上是容器操作);

为此， `Python` 定义了两个非常重要的宏，用于维护对象应用计数。
其中， `Py_INCREF` 将对象应用计数加一( *3* 行)：

.. code-block:: c
    :linenos:

    #define Py_INCREF(op) (                         \
        _Py_INC_REFTOTAL  _Py_REF_DEBUG_COMMA       \
        ((PyObject *)(op))->ob_refcnt++)

`Py_DECREF` 将引用计数减一( *5* 行)，并在引用计数为 *0* 是回收对象( *8* 行)：

.. code-block:: c
    :linenos:

    #define Py_DECREF(op)                                   \
        do {                                                \
            PyObject *_py_decref_tmp = (PyObject *)(op);    \
            if (_Py_DEC_REFTOTAL  _Py_REF_DEBUG_COMMA       \
            --(_py_decref_tmp)->ob_refcnt != 0)             \
                _Py_CHECK_REFCNT(_py_decref_tmp)            \
            else                                            \
                _Py_Dealloc(_py_decref_tmp);                \
        } while (0)

当一个对象引用计数为 *0* ， `Python` 便调用对象对应的析构函数回收对象，但这并不意味着对象内存一定会回收。
为了提高内存分配效率， `Python` 为一些常用对象维护了内存池，
对象回收后内存进入内存池中，以便下次使用，由此 **避免频繁申请、释放内存** 。

**内存池** 技术作为程序开发的高级话题，需要更大的篇幅，放在后续章节中介绍。
