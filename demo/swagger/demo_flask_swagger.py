from fishbase.swagger import doc
from fishbase.swagger.swagger import flask_swagger
from flask import Flask

# 创建 Flask app
app = Flask("Demo Server")
# Swagger 可以从 app 中读取配置信息
app.config.update({
    "API_VERSION": "v1.0.0",
    "NAME": "Demo Server",
    "API_DESCRIPTION": "Demo Server"
})


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


@app.route('/v1/query', methods=['GET'])
@doc.summary("xx业务查询接口", group="xx业务")
@doc.description("测试 Swagger 使用, 参数为 URL 参数 token, 且必传")
@doc.consumes("token", required=True)
def test_query():
    return "test_query"


@app.route('/v1/add', methods=['POST'])
@doc.summary("xx业务新增接口", group="xx业务")
@doc.description("测试 Swagger 使用, 参数为 URL 参数 token, 且必传和 AddXxReqVo 中的参数")
@doc.consumes(AddXxReqVo, location="body")
@doc.consumes("token", required=True)
def test_add():
    return "test_add"


@app.route('/v1/del', methods=['DELETE'])
@doc.summary("xx业删除增接口", group="xx业务")
@doc.description("测试 Swagger 使用, 参数为 URL 参数 token, 且非必传")
@doc.consumes("token", required=False)
def test_del():
    return "test_del"


@app.route('/v1/update', methods=['PUT'])
@doc.summary("xx业务更新接口", group="xx业务")
@doc.description("测试 Swagger 使用, 参数为 URL 参数 token, 且必传")
@doc.consumes(UpdateXxReqVo, location="body")
@doc.consumes("token", required=True)
def test_update():
    return "test_update"


# 将 app 对象传递给 swagger 模块
flask_swagger(app)

if __name__ == "__main__":
    app.run("127.0.0.1", "8899", debug=False)
