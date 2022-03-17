import asyncio
import time

import pynng

from config import node_activity_time
from utils.logging import logging
from .constant import GET_SERVICE_ADDRESS, REGISTER_SERVICE_ADDRESS
from .muti_reqrep import send_req_with_id, get_rep_by_id


def get_ttl_hash():
    """Return the same value withing `seconds` time period"""
    return round(time.time() / node_activity_time)


async def keep_register_service_address_list(address, self_address_list):
    with pynng.Req0() as sock:
        sock.dial(address)
        while True:
            for self_address in self_address_list:
                await _register_service_address(sock, self_address)
            await asyncio.sleep(node_activity_time / 2)


async def register_service_address(address, self_address):
    with pynng.Req0() as sock:
        sock.dial(address)
        await _register_service_address(sock, self_address)


async def _register_service_address(sock, self_address):
    data = f"{REGISTER_SERVICE_ADDRESS}{self_address}".encode()
    await send_req_with_id(sock, data)


# noinspection PyUnusedLocal
# @alru_cache(maxsize=1)
async def get_service_address_list(address, list_size=0, ttl_hash=get_ttl_hash()) -> list[str]:
    with pynng.Req0() as sock:
        sock.dial(address)
        if list_size:
            list_size_str = list_size
        else:
            list_size_str = ''
        msg = f"{GET_SERVICE_ADDRESS}{list_size_str}"
        msg_id = await send_req_with_id(sock, msg.encode())
        msg = await get_rep_by_id(sock, msg_id)
        service_address_list = msg.decode().split(' ')
        if not service_address_list:
            logging.warning("get_service_address_list: empty service list")
        return service_address_list
