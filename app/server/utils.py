import asyncio
import logging
from multiprocessing import Manager

from colorlog import ColoredFormatter
from requests import Response

from app.server.hubs import hub_script_utils

LOG_LEVEL = logging.DEBUG
LOG_FORMAT = "  %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"


def __init_logging():
    logging.root.setLevel(LOG_LEVEL)
    formatter = ColoredFormatter(LOG_FORMAT)
    stream = logging.StreamHandler()
    stream.setLevel(LOG_LEVEL)
    stream.setFormatter(formatter)
    log = logging.getLogger('base_logger')
    log.setLevel(LOG_LEVEL)
    log.addHandler(stream)
    return log


logging = __init_logging()


def get_response(url: str, throw_error=False, **kwargs) -> Response or None:
    return hub_script_utils.http_get(url, throw_error, **kwargs)


def set_new_asyncio_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.set_debug(True)
    return loop


def call_def_in_loop_return_result(core, loop):
    try:
        return loop.run_until_complete(core)
    except RuntimeError:
        future = asyncio.run_coroutine_threadsafe(core, loop)
    return future.result()


def call_def_in_loop(core, loop):
    try:
        loop.run_until_complete(core)
    except RuntimeError:
        asyncio.run_coroutine_threadsafe(core, loop)


def call_fun_list_in_loop(core_list: list, loop=set_new_asyncio_loop()):
    data_list = call_def_in_loop_return_result(asyncio.gather(*core_list), loop)
    return data_list


def grcp_dict_list_to_dict(grcp_dict: list or None) -> dict:
    d = {}
    if grcp_dict:
        for gd in grcp_dict:
            d[gd.key] = gd.value
    return d


__manager = Manager()


def get_manager_lock():
    return __manager.Lock()


def get_manager_value(key, value):
    return __manager.Value(key, value)


def get_manager_list():
    return __manager.list()


def get_manager_dict():
    return __manager.dict()
