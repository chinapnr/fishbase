"""

``fish_http_status`` 包含最通用的一些网络状态码

https://github.com/openstack/swift/blob/master/swift/common/http.py

"""


def is_informational(status):
    """
    检查状态码是否信息提示

    :param:
        * status: http 状态码
    :return:
        * result: True or False
    """
    return 100 <= status <= 199


def is_success(status):
    """
    检查状态码是否成功

    :param:
        * status: http 状态码
    :return:
        * result: True or False
    """
    return 200 <= status <= 299


def is_redirection(status):
    """
    检查状态码是否重定向

    :param:
        * status: http 状态码
    :return:
        * result: True or False
    """
    return 300 <= status <= 399


def is_client_error(status):
    """
    检查状态码是否客户端错误

    :param:
        * status: http 状态码
    :return:
        * result: True or False
    """
    return 400 <= status <= 499


def is_server_error(status):
    """
    检查状态码是否服务端错误

    :param:
        * status: http 状态码
    :return:
        * result: True or False
    """
    return 500 <= status <= 599


# List of HTTP status codes

###############################################################################
# 1xx Informational
###############################################################################


HTTP_CONTINUE = 100
HTTP_SWITCHING_PROTOCOLS = 101
HTTP_PROCESSING = 102  # WebDAV
HTTP_CHECKPOINT = 103
HTTP_REQUEST_URI_TOO_LONG = 122

###############################################################################
# 2xx Success
###############################################################################

HTTP_OK = 200
HTTP_CREATED = 201
HTTP_ACCEPTED = 202
HTTP_NON_AUTHORITATIVE_INFORMATION = 203
HTTP_NO_CONTENT = 204
HTTP_RESET_CONTENT = 205
HTTP_PARTIAL_CONTENT = 206
HTTP_MULTI_STATUS = 207  # WebDAV
HTTP_IM_USED = 226

###############################################################################
# 3xx Redirection
###############################################################################

HTTP_MULTIPLE_CHOICES = 300
HTTP_MOVED_PERMANENTLY = 301
HTTP_FOUND = 302
HTTP_SEE_OTHER = 303
HTTP_NOT_MODIFIED = 304
HTTP_USE_PROXY = 305
HTTP_SWITCH_PROXY = 306
HTTP_TEMPORARY_REDIRECT = 307
HTTP_RESUME_INCOMPLETE = 308

###############################################################################
# 4xx Client Error
###############################################################################

HTTP_BAD_REQUEST = 400
HTTP_UNAUTHORIZED = 401
HTTP_PAYMENT_REQUIRED = 402
HTTP_FORBIDDEN = 403
HTTP_NOT_FOUND = 404
HTTP_METHOD_NOT_ALLOWED = 405
HTTP_NOT_ACCEPTABLE = 406
HTTP_PROXY_AUTHENTICATION_REQUIRED = 407
HTTP_REQUEST_TIMEOUT = 408
HTTP_CONFLICT = 409
HTTP_GONE = 410
HTTP_LENGTH_REQUIRED = 411
HTTP_PRECONDITION_FAILED = 412
HTTP_REQUEST_ENTITY_TOO_LARGE = 413
HTTP_REQUEST_URI_TOO_LONG = 414
HTTP_UNSUPPORTED_MEDIA_TYPE = 415
HTTP_REQUESTED_RANGE_NOT_SATISFIABLE = 416
HTTP_EXPECTATION_FAILED = 417
HTTP_IM_A_TEAPOT = 418
HTTP_UNPROCESSABLE_ENTITY = 422  # WebDAV
HTTP_LOCKED = 423  # WebDAV
HTTP_FAILED_DEPENDENCY = 424  # WebDAV
HTTP_UNORDERED_COLLECTION = 425
HTTP_UPGRADE_REQUIED = 426
HTTP_PRECONDITION_REQUIRED = 428
HTTP_TOO_MANY_REQUESTS = 429
HTTP_REQUEST_HEADER_FIELDS_TOO_LARGE = 431
HTTP_NO_RESPONSE = 444
HTTP_RETRY_WITH = 449
HTTP_BLOCKED_BY_WINDOWS_PARENTAL_CONTROLS = 450
HTTP_CLIENT_CLOSED_REQUEST = 499

###############################################################################
# 5xx Server Error
###############################################################################

HTTP_INTERNAL_SERVER_ERROR = 500
HTTP_NOT_IMPLEMENTED = 501
HTTP_BAD_GATEWAY = 502
HTTP_SERVICE_UNAVAILABLE = 503
HTTP_GATEWAY_TIMEOUT = 504
HTTP_VERSION_NOT_SUPPORTED = 505
HTTP_VARIANT_ALSO_NEGOTIATES = 506
HTTP_INSUFFICIENT_STORAGE = 507  # WebDAV
HTTP_BANDWIDTH_LIMIT_EXCEEDED = 509
HTTP_NOT_EXTENDED = 510
HTTP_NETWORK_AUTHENTICATION_REQUIRED = 511
HTTP_NETWORK_READ_TIMEOUT_ERROR = 598     # not used in RFC
HTTP_NETWORK_CONNECT_TIMEOUT_ERROR = 599  # not used in RFC
