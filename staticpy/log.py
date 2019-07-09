import logging


log = logging.getLogger(__name__)
c_format = logging.Formatter(
    "%(levelname)s:[%(module)s#%(funcName)s, line %(lineno)d]: %(message)s")
c_handler = logging.StreamHandler()
c_handler.setFormatter(c_format)
log.addHandler(c_handler)