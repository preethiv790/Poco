# -*- coding: utf-8 -*-
# @Author: gzliuxin
# @Email:  gzliuxin@corp.netease.com
# @Date:   2017-07-14 19:47:51
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from poco.interfaces.rpc import RpcInterface
from poco.vendor.mh.simplerpc.simplerpc import Connection
from poco.vendor.mh.simplerpc.rpcclient import RpcClient
from poco.vendor.mh.mh_rpc import sync_wrapper
from threading import Thread
from poco import Poco
import time


DEFAULT_ADDR = ('', 5001)


class CocosJsPoco(Poco):
    """docstring for CocosJsPoco"""
    def __init__(self, addr=DEFAULT_ADDR):
        self._rpc_client = SocketIORpc(addr)
        super(CocosJsPoco, self).__init__(self._rpc_client, action_interval=0.01)


class SimpleWS(WebSocket):

    def __init__(self, *args, **kwargs):
        super(SimpleWS, self).__init__(*args, **kwargs)
        self._inbox = []

    def handleMessage(self):
        print(self.data)
        self._inbox.append(self.data)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

    def swapMessage(self):
        msg, self._inbox = self._inbox, []
        return msg


class SocketIORpc(RpcInterface):
    def __init__(self, addr=DEFAULT_ADDR):
        conn = SocketIOConnection(addr)
        self.c = RpcClient(conn)

    @sync_wrapper
    def dump(self):
        return self.c.call("dump")


class SocketIOConnection(Connection):
    def __init__(self, addr):
        self.server = self.init_server(addr[0], addr[1])
        self.client_index = 0

    @staticmethod
    def init_server(host, port):
        server = SimpleWebSocketServer(host, port, SimpleWS)
        t = Thread(target=server.serveforever)
        t.daemon = True
        t.start()
        return server

    @property
    def client(self):
        try:
            c = self.server.connections.values()[self.client_index]
        except IndexError:
            raise RuntimeError("client %s not connected" % self.client_index)
        return c

    def connect(self):
        for i in range(10):
            if self.server.connections:
                return True
            time.sleep(1)
            print("wait for client")
        raise RuntimeError("no client connected")

    def send(self, msg):
        if isinstance(msg, str):
            msg = msg.decode("utf-8")
        self.client.sendMessage(msg)

    def recv(self):
        messages = self.server.swapMessage()
        return messages