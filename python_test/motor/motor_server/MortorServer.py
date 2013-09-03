 
from MotorWork import MotorWork
from motor import  Motor
import MortorServerInfo 
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
config = MortorServerInfo.getMotorServerConfig()
motorHandler = MotorWork()
processor = Motor.Processor(motorHandler)
transport = TSocket.TServerSocket(config['SERVER_IP'], config['SERVER_PORT'])
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
 
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
 
print "Starting thrift server in python..."
server.serve()
print "done!"