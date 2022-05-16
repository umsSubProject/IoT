import socket
from time import sleep
from config.parameter import Comms

class DataComms():
    def __init__(self,name:str, ip:str, port:int, protocol:bool):
        self.name = name
        self.ip = ip
        self.port = port
        self.protocol = protocol  # True : TCP, False : UDP

        self._runServer = True
        self._readyServer = False
        self._runClient = True
        self._readyClient = False
    
    def _open_server(self) -> socket.socket:
        funcName = '_open_server'
        COMMS_ADDRESS = self.ip
        timeout = Comms.SOCKET_TIMEOUT
        while not self._readyServer:
            try:
                if self.protocol == True:
                    tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    tcpServer.bind(COMMS_ADDRESS)
                    tcpServer.listen()
                    if timeout != None and type(timeout) == int: tcpServer.settimeout(timeout)
                    self._readyServer = True
            except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError) as err:
                self._readyServer = False
                tcpServer.close()
                sleep(Comms.RECONNECTION_TIMER)
            try:
                if self.protocol == False:
                    udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    udpServer.bind(COMMS_ADDRESS)
                    self._readyServer = True
            except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError) as err:
                self._readyServer = False
                udpServer.close()
                sleep(Comms.RECONNECTION_TIMER)
        if self.protocol:
            return tcpServer
        elif not self.protocol:
            return udpServer
    
    def main_server(self):
        funcName = 'main_server'

        while self._runServer:
            if not self._readyServer:
                mainServer = self._open_server()
                
class Mqtt():
    def __init(self):
        pass