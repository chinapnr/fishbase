from fishbase.swagger import doc
from fishbase.swagger.swagger import flask_swagger
from flask import Blueprint, Flask

# 创建 Flask app
app = Flask("Demo Server")
# Swagger 可以从 app 中读取配置信息
app.config.update({
    "API_VERSION": "v1.0.0",
    "NAME": "Demo Server",
    "API_DESCRIPTION": "Demo Server"
})
# 创建 Flask 蓝图
APPBlueprint = Blueprint(name='', import_name=__name__)


class AddXxReqVo:
    """
    新增 Xx 请求 Vo
    """
    name = ""
    age = 0


class UpdateXxReqVo:
    """
    更新 Xx 请求 Vo
    """
    name = ""
    age = 0


@doc.summary("xx业务查询接口", group="xx业务")
@doc.description("测试 Swagger 使用, 实例采用蓝图的方式, 参数为 URL 参数 token, 且必传")
@doc.consumes("token", required=True)
def test_query():
    pass


@doc.summary("xx业务新增接口", group="xx业务")
@doc.description("测试 Swagger 使用, 实例采用蓝图的方式, 参数为 URL 参数 token, 且必传和 AddXxReqVo 中的参数")
@doc.consumes(AddXxReqVo, location="body")
@doc.consumes("token", required=True)
def test_add():
    pass


@doc.summary("xx业删除增接口", group="xx业务")
@doc.description("测试 Swagger 使用, 实例采用蓝图的方式, 参数为 URL 参数 token, 且非必传")
@doc.consumes("token", required=False)
def test_del():
    pass


@doc.summary("xx业务更新接口", group="xx业务")
@doc.description("测试 Swagger 使用, 实例采用蓝图的方式, 参数为 URL 参数 token, 且必传")
@doc.consumes(UpdateXxReqVo, location="body")
@doc.consumes("token", required=True)
def test_update():
    pass


# 定义路由信息, 并指定路由映射的方法，请求方式等
APPBlueprint.add_url_rule(f'/v1/query', view_func=test_query, methods=['GET'], endpoint='test_func1')
APPBlueprint.add_url_rule(f'/v1/add', view_func=test_add, methods=['POST'], endpoint='test_func2')
APPBlueprint.add_url_rule(f'/v1/del', view_func=test_del, methods=['DELETE'], endpoint='test_func3')
APPBlueprint.add_url_rule(f'/v1/update', view_func=test_update, methods=['PUT'], endpoint='test_func4')

app.register_blueprint(APPBlueprint)
# 将 app 对象传递给 swagger 模块
flask_swagger(app)

if __name__ == "__main__":
    app.run("127.0.0.1", "8899", debug=False)
