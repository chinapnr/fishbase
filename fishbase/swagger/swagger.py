import os

try:
    from flask import Blueprint, jsonify, render_template
except Exception as e:
    pass

from .doc import route_specs, serialize_schema, definitions

dir_path = os.path.dirname(os.path.realpath(__file__))
static_path = os.path.abspath(dir_path + "/static")
template_path = os.path.abspath(dir_path + "/templates")

# 配置对象
_swagger_json = {}
_swagger_config = {}

# swagger 蓝图
swagger_blueprint = Blueprint(name="swagger", import_name=__name__, url_prefix="/swagger",
                              template_folder=template_path, static_folder=static_path)


class SwaggerHelper:
    _type_map = {str: "string", int: "int"}

    @staticmethod
    def app_is_debug(app):
        return getattr(app.config, "DEBUG", True)

    @staticmethod
    def get_api_method(rule):
        """
        获取路由方法，给每种方法打分，优先级 delete -> patch -> post -> get -> options -> head
        :param rule:
        :return:
        """
        method_option = ["delete", "put", "patch", "post", "get", "options", "head"]  # 优先级越高,索引最小，返回最高优先级方法
        return method_option[min([method_option.index(x.lower()) for x in rule.methods])]

    @staticmethod
    def consumes_content_types(app, _rule_specs):
        """
        入参类型
        :return:
        """
        api_consumes_content_types = app.config.get("API_CONSUMES_CONTENT_TYPES", ["application/json"])
        consumes_content_types = (
                _rule_specs.consumes_content_type or api_consumes_content_types
        )
        return consumes_content_types

    @staticmethod
    def app_name(app):
        """
        入参类型
        :return:
        """
        app_name = app.config.get("NAME", "API")
        return app_name

    @staticmethod
    def produces_content_types(app, _rule_specs):
        """
        结果出参格式
        :param app:
        :param _rule_specs:
        :return:
        """
        api_produces_content_types = app.config.get("API_PRODUCES_CONTENT_TYPES", ["application/json"])
        produces_content_types = (
                _rule_specs.produces_content_type or api_produces_content_types
        )
        return produces_content_types

    @staticmethod
    def get_route_parameters(_rule_specs):
        """
        参数
        :param _rule_specs:
        :return:
        """
        route_parameters = []
        for consumer in _rule_specs.consumes:
            spec = serialize_schema(consumer.field)
            if "properties" in spec:
                for name, prop_spec in spec["properties"].items():
                    route_param = {
                        **prop_spec,
                        "required": consumer.required,
                        "in": consumer.location,
                        "name": name,
                    }
            else:
                route_param = {
                    **spec,
                    "required": consumer.required,
                    "in": consumer.location,
                    "name": "body"
                }

            if "$ref" in route_param:
                route_param["schema"] = {"$ref": route_param["$ref"]}
                del route_param["$ref"]

            route_parameters.append(route_param)
        return route_parameters

    @staticmethod
    def get_responses(_rule_specs):
        """
        响应
        :param _rule_specs:
        :return:
        """
        responses = {}
        if len(_rule_specs.response) == 0:
            responses["200"] = {
                "schema": serialize_schema(_rule_specs.produces.field)
                if _rule_specs.produces
                else None,
                "description": _rule_specs.produces.description
                if _rule_specs.produces
                else None,
            }

        for (status_code, routefield) in _rule_specs.response:
            responses["{}".format(status_code)] = {
                "schema": serialize_schema(routefield.field),
                "description": routefield.description,
            }
        return responses


def flask_swagger(app):
    """
    flask swagger
    :param app:
    :return:
    """
    if not SwaggerHelper.app_is_debug(app):
        return

    # 更新路由
    app.register_blueprint(swagger_blueprint)

    # 更新swagger 配置
    _swagger_json["definitions"] = {}
    _swagger_json["swagger"] = "2.0"
    _swagger_json["info"] = {
        "version": app.config.get("API_VERSION", "1.0.0"),
        "title": app.config.get("NAME", "API"),
        "description": app.config.get("API_DESCRIPTION", ""),
        "termsOfService": app.config.get("API_TERMS_OF_SERVICE", "HuiFu"),
        "contact": {"email": app.config.get("API_CONTACT_EMAIL", "")},
        "license": {
            "name": app.config.get("API_LICENSE_NAME", None),
            "url": app.config.get("API_LICENSE_URL", None)
        },
    }
    _swagger_json["schemes"] = app.config.get("PREFERRED_URL_SCHEME", ["http"])
    host = app.config.get("API_HOST", None)

    if host is not None:
        _swagger_json["host"] = host

    base_path = app.config.get("API_BASEPATH", None)
    if base_path is not None:
        _swagger_json["basePath"] = base_path

    # Authorization
    _swagger_json["securityDefinitions"] = app.config.get("API_SECURITY_DEFINITIONS", None)
    _swagger_json["security"] = app.config.get("API_SECURITY", None)

    # Tags
    _swagger_json["tags"] = [SwaggerHelper.app_name(app) or "Test"]

    # Router
    _swagger_json["paths"] = {}
    for rule in app.url_map._rules:
        _endpoint = rule.endpoint  # 当前路由 endpoint
        _method = SwaggerHelper.get_api_method(rule)  # 当前路由 method
        _view_func = app.view_functions.get(_endpoint)  # 获取当前路由方法对象
        _rule_specs = route_specs.get(_view_func)

        if not _rule_specs:
            continue

        # 主体
        body = {
            _method: {
                "operationId": _rule_specs.operation,
                "summary": _rule_specs.summary,
                "description": _rule_specs.description,
                "consumes": SwaggerHelper.consumes_content_types(app, _rule_specs),
                "produces": SwaggerHelper.produces_content_types(app, _rule_specs),
                # "tags": [SwaggerHelper.app_name(app) or "Test"],
                "tags": [_rule_specs.group],
                "parameters": SwaggerHelper.get_route_parameters(_rule_specs),
                "responses": SwaggerHelper.get_responses(_rule_specs),
            }
        }

        if _swagger_json["paths"].get(rule.rule):
            _swagger_json["paths"][rule.rule].update(body)
        else:
            _swagger_json["paths"][rule.rule] = body

    # Models
    _swagger_json["definitions"] = {
        obj.object_name: definition for obj, definition in definitions.values()
    }


def swagger_json():
    """
    返回 json 数据
    :return:
    """
    return jsonify(_swagger_json)


def swagger_config():
    """
    返回 config 数据
    :return:
    """
    return jsonify(_swagger_config)


def swagger():
    """
    返回页面
    :return:
    """
    return render_template("index.html")


swagger_blueprint.add_url_rule(f'/swagger.json', view_func=swagger_json, methods=['GET'], endpoint='swagger_json')
swagger_blueprint.add_url_rule(f'/swagger-config', view_func=swagger_json, methods=['GET'], endpoint='swagger_config')
swagger_blueprint.add_url_rule(f'/', view_func=swagger, methods=['GET'], endpoint='swagger')
