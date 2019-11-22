``swagger`` 为 flask 应用生成接口文档信息
=========================================

简单 flask 应用
-----------------------------------------------

.. code:: python

   >>> from fishbase.swagger import doc
   >>> from fishbase.swagger.swagger import flask_swagger
   >>> from flask import Flask

   >>> # 创建 Flask app
   >>> app = Flask("Demo Server")

   >>> @app.route('/v1/query', methods=['GET'])
   >>> @doc.summary("xx业务查询接口", group="xx业务")
   >>> @doc.description("测试 Swagger 使用, 参数为 URL 参数 token, 且必传")
   >>> @doc.consumes("token", required=True)
   >>> def test_query():
   >>>     pass

   >>> # 将 app 对象传递给 swagger 模块
   >>> flask_swagger(app)

   >>> if __name__ == "__main__":
   >>>     app.run("127.0.0.1", "8899", debug=False)

访问: http://ip:port/swagger 即可查看接口信息。更多示例，可参考 :meth:`demo/demo_flask_swagger.py`


蓝图模式的 flask 应用
-----------------------------------------------

.. code:: python

    >>> from fishbase.swagger import doc
    >>> from fishbase.swagger.swagger import flask_swagger
    >>> from flask import Blueprint, Flask

    >>> # 创建 Flask app
    >>> app = Flask("Demo Server")
    >>> # Swagger 可以从 app 中读取配置信息
    >>> app.config.update({
    >>>     "API_VERSION": "v1.0.0",
    >>>     "NAME": "Demo Server",
    >>>     "API_DESCRIPTION": "Demo Server"
    >>> })
    >>> # 创建 Flask 蓝图
    >>> APPBlueprint = Blueprint(name='', import_name=__name__)

    >>> @doc.summary("xx业务查询接口", group="xx业务")
    >>> @doc.description("测试 Swagger 使用, 实例采用蓝图的方式, 参数为 URL 参数 token, 且必传")
    >>> @doc.consumes("token", required=True)
    >>> def test_query():
    >>>     pass

    >>> # 定义路由信息, 并指定路由映射的方法，请求方式等
    >>> APPBlueprint.add_url_rule('/v1/query', view_func=test_query, methods=['GET'], endpoint='test_func1')

    >>> app.register_blueprint(APPBlueprint)
    >>> # 将 app 对象传递给 swagger 模块
    >>> flask_swagger(app)

    >>> if __name__ == "__main__":
    >>>    app.run("127.0.0.1", "8899", debug=False)


访问:  http://ip:port/swagger  即可查看接口信息。更多示例，可参考 :meth:`demo/demo_flask_blueprint_swagger.py`

使用技巧
-----------------------------------------------
1. 如何启用？
    只需调用 flask_swagger，并传入 flask app 对象即可。

2. 如何关闭？
    只需将在 app 配置中将DEBUG设置为 False 即可关闭此功能。

3. 如何添加接口摘要信息？
    若想在文档中添加摘要信息，需在对应方法上添加 :meth:`@doc.summary("xx业务查询接口", group="xx业务")` 装饰器。其中第一个参数为摘要描述信息，可选参数 group 可将接口进行分组

4. 如何添加接口描述信息？
    若想在文档中添加描述信息，需在对应方法上添加 :meth:`@doc.description("测试 Swagger 使用, 实例采用蓝图的方式, 参数为 URL 参数 token, 且必传")` 装饰器。参数即为描述内容

5. 参数为 url 参数时如何配置？
    若参数为 url 参数， 需在对应方法上添加 :meth:`@doc.consumes("token", required=True)` 装饰器，其中第一个参数为参数名称，可选参数 required 代表此参数是否必传，默认为 False。可选参数 location 代表此参数传递的位置，默认为 query。

6. 参数为请求体参数时如何配置？
    若参数为请求体参数，使用方法与参数为 url 参数类似，只需将第一个参数改为请求体参数对象(可以是一个类，或者字典)。location 设置为 body。例如： :meth:`@doc.consumes(AddXxReqVo, location="body")`

7. 如何进行接口在线调试？
    使用 swagger，并且项目正常启动后，访问 http://ip:port/swagger 即可看到 flask app 所拥有的所有接口信息，点击 Try it out 即可进行在线调试。注意：为了安全起见，建议项目在生产环境运行时候关闭 swagger 功能，只需将 app 对象中的 DEBUG 设置为 False 即可。


更多源码信息
-----------------------------------------------
.. autosummary::
    swagger.swagger.flask_swagger
    swagger.swagger.swagger_json
    swagger.swagger.swagger_config
    swagger.swagger.swagger

.. automodule:: swagger.swagger
   :members:
