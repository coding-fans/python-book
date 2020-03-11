..
    Author: fasion
    Created time: 2020-03-09 18:01:42
    Last Modified by: fasion
    Last Modified time: 2020-03-11 11:33:00

.. meta::
    :description lang=zh:
        本教程译自PyMongo官方教程Pymongo Tutorial，旨在介绍Pymongo操作MongoDB的基本用法，以快速形成开发能力。
    :keywords: python, mongodb, pymongo, 中文, 教程, 文档

================
PyMongok简明教程
================

本教程译自 `PyMongo`_ 官方教程 `PyMongo Tutorial`_ ，旨在介绍 *PyMongo* 操作 *MongoDB* 的基本用法，以快速形成开发能力。

准备环境
========

开始之前，需要先安装 *PyMongo* 包，一般使用 *pip* 命令即可：

.. code-block:: shell-session

    $ pip install pymongo

*PyMongo* 报安装完毕后，即可将其 *import* 到程序中：

.. code-block:: pycon

    >>> import pymongo

本教程假设你本地已经部署好 *MongoDB* 服务，且采用默认端口。

如果你还没准备好 *MongoDB* 服务，可以参考官网文档下载并部署 *MongDB* 。

开发环境更推荐采用 *Docker* 容器化部署，以降低维护成本。
*Docker* 快速使用指引请看考这篇文章：`前端工程师眼中的 Docker <https://nodejs.fasionchan.com/zh_CN/latest/practices/docker/introduce.html>`_ 。
*MongoDB* 镜像可以在 `Docker Hub`_ 上找到。

建立连接
========

使用 *PyMongo* 第一步，创建 MongoClient 对象以连接数据库实例。
操作毫无难度：

.. code-block:: pycon

    >>> from pymongo import MongoClient
    >>> client = MongoClient()

*MongoClient* 默认连接本地的 *MongoDB* 端口，当然了，显示指定也可以：

.. code-block:: pycon

    >>> client = MongoClient('localhost', 27017)

此外，还可以使用 MongoDB  URI 格式字符串：

.. code-block:: pycon

    >>> client = MongoClient('mongodb://localhost:27017/')

操作数据库
==========

单个 *MongoDB* 实例可以运行多个数据库，数据库是互相独立的。
使用 *PyMongo* 时，通过 *MongoClient* 属性即可访问指定数据库：

.. code-block:: pycon

    >>> db = client.test_database

如果你的数据库名不是一个合法的属性名，便只能以 *dict* 风格来访问了：

.. code-block:: pycon

    >>> db = client['test-database']

登录授权
========


操作集合（表）
==============

*MongoDB* 中的 **集合** ( *collection* )用于保存 **文档** ( *document* )，可以粗略看做关系型数据库中的 **表** ( *table* )。
操作集合的方式与操作数据库类似，分为 **属性访问** 风格：

.. code-block:: pycon

    >>> collection = db.test_collection

以及 **字典访问** 风格：

.. code-block:: pycon

    >>> collection = db['test-collection']

文档
====

*MongoDB* 中的数据以 **文档** 的形式表示、存储，文档结构为 *JSON* 风格， *PyMongo* 则用 **字典** ( *dict* )来表示文档。
举个例子，下面这个 *dict* 可以用来组织一篇博文( *post* )：

.. code-block:: pycon

    >>> import datetime
    >>> post = {"author": "Mike",
    ...         "text": "My first blog post!",
    ...         "tags": ["mongodb", "python", "pymongo"],
    ...         "date": datetime.datetime.utcnow()}

注意到，文档可以包含 *Python* 原生数据类型(如 *datetime.datetime* 对象)， *PyMongo* 会自动转成 *BSON* 类型。

插入文档
========

将文档插入集合，只需调用 *insert_one* 方法：

.. code-block:: pycon

    >>> posts = db.posts
    >>> post_id = posts.insert_one(post).inserted_id
    >>> post_id
    ObjectId('...')

每个文档都必须包括一个 *_id* 字段，该字段值在集合中是唯一的。
如果待插入文档没有提供 *_id* 字段， *PyMongo* 将自动生成一个。
*insert_one* 方法返回一个 *InsertOneResult* 类型实例，从中可以取出成功插入的文档 *ID* 。
文档 *ID* 的详细介绍，请查看 *MongoDB* 官方文档： `ObjectID`_ 。

集合无须提前建好，首次操作时数据库将自动创建。
列举数据库所有集合即可看到：

.. code-block:: pycon

    >>> db.list_collection_names()
    [u'posts']

查询文档
========

在 *MongoDB* 中，最基本的查询方法是 `find_one`_ 。
*find_one* 返回命中查询条件的第一个文档，没有文档命中则返回 *None* 。
确定查询结果只有一个，或者只须处理第一个时，用 *find_one* 就恰到好处。
下面这个例子通过 *find_one* 获取 *posts* 集合中的第一个：

.. code-block:: pycon

    >>> import pprint
    >>> pprint.pprint(posts.find_one())
    {u'_id': ObjectId('...'),
     u'author': u'Mike',
     u'date': datetime.datetime(...),
     u'tags': [u'mongodb', u'python', u'pymongo'],
     u'text': u'My first blog post!'}

查询结果是一个 *dict* 对象，内容跟我们在上一小节中插入的一样。

*find_one* 支持指定 **查询条件** ，来检索符合条件的文档。
例如，查找一篇由 *Mike* 创作的博文：

.. code-block:: pycon

    >>> pprint.pprint(posts.find_one({"author": "Mike"}))
    {u'_id': ObjectId('...'),
     u'author': u'Mike',
     u'date': datetime.datetime(...),
     u'tags': [u'mongodb', u'python', u'pymongo'],
     u'text': u'My first blog post!'}

.. note::

    注意到，返回文档包含 *_id* 字段，这是插入时自动添加的。

尝试以另一个作者来查询，比如 *Eliot* ，则得不到任何东西：

.. code-block:: pycon

    >>> posts.find_one({"author": "Eliot"})
    >>>

用 ObjectID 查询
================

我们也可以通过 *_id* 字段来查找博文，该字段是一个 `ObjectID`_ ：

.. code-block:: pycon

    >>> post_id
    ObjectId(...)
    >>> pprint.pprint(posts.find_one({"_id": post_id}))
     {u'_id': ObjectId('...'),
     u'author': u'Mike',
     u'date': datetime.datetime(...),
     u'tags': [u'mongodb', u'python', u'pymongo'],
     u'text': u'My first blog post!'}

需要特别注意的是， *ObjectId* 与它的字符串形式是不同的：

.. code-block:: pycon

    >>> post_id_as_str = str(post_id)
    >>> posts.find_one({"_id": post_id_as_str}) # No result
    >>>

在 *Web* 应用有一个很常见的场景，从 *URL* 中取出 *ObjectID* ，再从数据库中查询对应的文档。
切记，在将 *_id* 传给 *find_one* 前，需要将其从字符串转化成 *ObjectID* ：

.. code-block:: python

    from bson.objectid import ObjectId

    # The web framework gets post_id from the URL and passes it as a string
    def get(post_id):
        # Convert from string to ObjectId:
        document = client.db.collection.find_one({'_id': ObjectId(post_id)})

批量插入
========

为了演示更有趣的查询方式，我们需要往 *posts* 集合中插入更多文档。
除了逐个插入，我们还可以执行 **批量插入** ，将包含文档的 *list* 对象作为第一参数传给 `insert_many`_ 。
这个操作只向数据库发送一个指令，便插入 *list* 中所有文档：

.. code-block:: pycon

    >>> new_posts = [{"author": "Mike",
    ...               "text": "Another post!",
    ...               "tags": ["bulk", "insert"],
    ...               "date": datetime.datetime(2009, 11, 12, 11, 14)},
    ...              {"author": "Eliot",
    ...               "title": "MongoDB is fun",
    ...               "text": "and pretty easy too!",
    ...               "date": datetime.datetime(2009, 11, 10, 10, 45)}]
    >>> result = posts.insert_many(new_posts)
    >>> result.inserted_ids
    [ObjectId('...'), ObjectId('...')]

关于这个例子，我们还需要关注以下两点：

- *insert_many* 返回结果中包含两个 *ObjectId* ，每个文档各一个；
- 文档 ``new_posts[1]`` 与其他文档结构不同，它没有 *tags* 字段，缺多了一个新字段 *title* 。
  这就是我们说 *MongoDB* 是 **无模式** ( *schema free* )数据库的原因。

多文档查询
==========

除了单个文档，我们还可以通过 `find`_ 方法检索符合查询条件的多个文档。
*find* 方法返回 `Cursor`_ （ **游标** )对象，迭代游标对象即可遍历查询结果。
举个例子，我们可以这样遍历 *posts* 集合中的每个文档：

.. code-block:: pycon

    >>> for post in posts.find():
    ...   pprint.pprint(post)
    ...
    {u'_id': ObjectId('...'),
     u'author': u'Mike',
     u'date': datetime.datetime(...),
     u'tags': [u'mongodb', u'python', u'pymongo'],
     u'text': u'My first blog post!'}
    {u'_id': ObjectId('...'),
     u'author': u'Mike',
     u'date': datetime.datetime(...),
     u'tags': [u'bulk', u'insert'],
     u'text': u'Another post!'}
    {u'_id': ObjectId('...'),
     u'author': u'Eliot',
     u'date': datetime.datetime(...),
     u'text': u'and pretty easy too!',
     u'title': u'MongoDB is fun'}

跟 *find_one* 一样，我们可以将 **查询条件** 作为参数传给 *find* ，以此匹配需返回的文档。
这里我们检索所有作者为 *Mike* 的所有博文：

.. code-block:: pycon

    >>> for post in posts.find({"author": "Mike"}):
    ...   pprint.pprint(post)
    ...
    {u'_id': ObjectId('...'),
     u'author': u'Mike',
     u'date': datetime.datetime(...),
     u'tags': [u'mongodb', u'python', u'pymongo'],
     u'text': u'My first blog post!'}
    {u'_id': ObjectId('...'),
     u'author': u'Mike',
     u'date': datetime.datetime(...),
     u'tags': [u'bulk', u'insert'],
     u'text': u'Another post!'}

计数
====

如果我们只须获悉符合查询条件的文档有多少，那么可以发起一个 `count_documents`_ 操作，无须全量查询。
我们既可查询集合的文档总数：

.. code-block:: pycon

    >>> posts.count_documents({})
    3

也可查询符合查询条件的文档数量：

.. code-block:: pycon

    >>> posts.count_documents({"author": "Mike"})
    2


范围查询
========

*MongDB* 支持形式多样的高级查询。
举个例子，我们可以执行一个查询，找出所有时间早于某天的博文，并按作者排序：

.. code-block:: pycon

    >>> d = datetime.datetime(2009, 11, 12, 12)
    >>> for post in posts.find({"date": {"$lt": d}}).sort("author"):
    ...   pprint.pprint(post)
    ...
    {u'_id': ObjectId('...'),
     u'author': u'Eliot',
     u'date': datetime.datetime(...),
     u'text': u'and pretty easy too!',
     u'title': u'MongoDB is fun'}
    {u'_id': ObjectId('...'),
     u'author': u'Mike',
     u'date': datetime.datetime(...),
     u'tags': [u'bulk', u'insert'],
     u'text': u'Another post!'}

这里，我们使用了特殊操作符 `$lt`_ 进行 **范围查询** ，并调用  `sort`_ 将结果排序。

索引
====

为集合添加索引，不仅可以加快特定查询，还能为文档查询、排序带来新能力。
本节演示如何为一个字段建立 **唯一索引** ( `unique index`_ )，确保该字段在集合内不会重复。

首先，我们需要建立索引：

.. code-block:: pycon

    >>> result = db.profiles.create_index([('user_id', pymongo.ASCENDING)],
    ...                                   unique=True)
    >>> sorted(list(db.profiles.index_information()))
    [u'_id_', u'user_id_1']

注意到，现在 *profiles* 已经有两个索引了：
其中一个建在 *_id* 字段上，这是 *MongoDB* 自动创建的；
另一个是我们刚为 *user_id* 字段创建的。

现在，我们加入一些个人档案：

.. code-block:: pycon

    >>> user_profiles = [
    ...     {'user_id': 211, 'name': 'Luke'},
    ...     {'user_id': 212, 'name': 'Ziltoid'}]
    >>> result = db.profiles.insert_many(user_profiles)

如果待插入文档 *user_id* 字段已被占用，唯一索引将阻止插入：

.. code-block:: pycon

    >>> new_profile = {'user_id': 213, 'name': 'Drew'}
    >>> duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
    >>> result = db.profiles.insert_one(new_profile)  # This is fine.
    >>> result = db.profiles.insert_one(duplicate_profile)
    Traceback (most recent call last):
    DuplicateKeyError: E11000 duplicate key error index: test_database.profiles.$user_id_1 dup key: { : 212 }

附录
====

.. include:: /_fragments/next-step-to-wechat-mp.rst

.. include:: /_fragments/wechat-reward.rst

.. include:: /_fragments/disqus.rst

.. _find: https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.find
.. _find_one: https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.find_one
.. _insert_many: https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.insert_many
.. _Cursor: https://api.mongodb.com/python/current/api/pymongo/cursor.html#pymongo.cursor.Cursor
.. _MongoDB: https://www.mongodb.com/
.. _ObjectID: http://www.mongodb.org/display/DOCS/Object+IDs
.. _PyMongo: https://api.mongodb.com/python/
.. _unique index: http://docs.mongodb.org/manual/core/index-unique/
.. _count_documents: https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.count_documents
.. _sort: https://api.mongodb.com/python/current/api/pymongo/cursor.html#pymongo.cursor.Cursor.sort
.. _$lt: https://docs.mongodb.com/manual/reference/operator/query/lt
.. _Docker Hub: https://hub.docker.com/_/mongo
.. _PyMongo Tutorial: https://api.mongodb.com/python/current/tutorial.html
