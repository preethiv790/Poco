# coding=utf-8

import base64
import time
import json

from poco.drivers.unity3d import UnityPoco
from poco.drivers.unity3d.unity3d_poco import DEFAULT_ADDR, Dumper
from poco.utils.simplerpc.rpcclient import RpcClient
from poco.utils.simplerpc.transport.tcp import TcpClient


def dump():
    conn = TcpClient(DEFAULT_ADDR)
    c = RpcClient(conn)
    c.DEBUG = False
    c.run(backend=True)
    time.sleep(2)
    t0 = time.time()
    d = Dumper(c)
    h = d.dumpHierarchy()
    t1 = time.time()
    print t1 - t0
    return h


if __name__ == '__main__':
    time.sleep(2)

    p = UnityPoco(DEFAULT_ADDR, unity_editor=True)
    b64img, fmt = p.snapshot()
    print b64img
    print len(b64img)
    print p.agent.get_debug_profiling_data()

    h = p.agent.hierarchy.dump()
    print json.dumps(h)
    print p.agent.get_debug_profiling_data()
    # img = open('img.png', 'wb')
    # img.write(base64.b64decode(b64img))
    # for n in p():
    #     print n.attr('components')

    # h = dump()
    # print json.dumps(h)