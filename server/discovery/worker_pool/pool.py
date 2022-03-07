import asyncio
import random
import time

import pynng

from config import node_activity_time, discovery_url
from ..client_utils import get_service_address_list


class Node:
    def __init__(self):
        self.socket = None
        self.time = None

    def init_socket(self, address: str):
        sock = pynng.Req0()
        sock.dial(address)
        self.socket = sock
        self.time = time.time()

    def self_check(self) -> bool:
        if time.time() - self.time > node_activity_time:
            self.disconnect()
            return False
        else:
            return True

    def disconnect(self):
        self.socket.close()


node_list: list[Node] = []
discovery_address = discovery_url
lock = asyncio.Lock()


async def get_node() -> Node or None:
    async with lock:
        return await _get_node()


async def _get_node() -> Node or None:
    node = _get_cache_node()
    if not node:
        await _renew_node_list()
        node = _get_cache_node(False)
    return node


def _get_cache_node(self_check=True) -> Node or None:
    if not node_list:
        return None
    node = random.choice(node_list)
    if not self_check:
        return node
    if node.self_check():
        return node
    else:
        node_list.remove(node)
        return None


async def _get_new_node() -> Node or None:
    server_list = await get_service_address_list(discovery_address)
    server_address = random.choice(server_list)
    node = Node()
    node.init_socket(server_address)
    return node


async def _renew_node_list():
    while len(node_list) <= 3:
        node = await _get_new_node()
        node_list.append(node)
