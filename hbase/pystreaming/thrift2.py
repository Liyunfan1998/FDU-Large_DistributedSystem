# -*- coding:utf-8 -*-
import sys
sys.path.append('/usr/local/hadoop/hive/lib/py')
from thrift.transport import TSocket
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport
from hbase import THBaseService

transport = TTransport.TBufferedTransport(TSocket.TSocket('127.0.0.1', 9090))
protocol = TBinaryProtocol.TBinaryProtocolAccelerated(transport)
client = THBaseService.Client(protocol)
transport.open()
# 使用 client 实例进行操作
# transport.close()
