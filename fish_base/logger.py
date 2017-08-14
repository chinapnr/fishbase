# 2017.3.5 edit by David.Yi , reference by Ucloud sdk
# 2017.3.15 edit by David.Yi
# 2017.6.20 edit by aoran.xue #14109
# 2017.8.14 move to fish_base

import logging
from logging.handlers import TimedRotatingFileHandler


LOG_FILE = 'default.log'

_formatter = logging.Formatter(
    '%(asctime)s %(levelname)s %(threadName)s[%(thread)d] %(filename)s[line:%(lineno)d] %(message)s')

_sh = logging.StreamHandler()
_sh.setLevel(logging.WARNING)
_sh.setFormatter(_formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(_sh)


def set_log_file(local_file=None):

    global LOG_FILE

    if local_file is not None:
        LOG_FILE = local_file

    # time rotating file handler
    _tfh = TimedRotatingFileHandler(LOG_FILE, when="midnight")
    _tfh.setLevel(logging.INFO)
    _tfh.setFormatter(_formatter)

    # logger.addHandler(_fh)
    logger.addHandler(_tfh)
