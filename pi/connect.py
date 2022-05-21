import socket
from time import sleep
from config.parameter import Sock

class TcpServer():
    def __init__(self,name:str, ip:str, port:int):
        self.name = name
        self.ip = ip
        self.port = port

        self._runServer = True
        self._readyServer = False
    
    def _open_tcp_server(self) -> socket.socket:
        funcName = '_open_tcp_server'
        COMMS_ADDRESS = self.ip
        timeout = Sock.SOCKET_TIMEOUT
        while not self._readyServer:
            try:
                tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                tcpServer.bind(COMMS_ADDRESS)
                tcpServer.listen()
                if timeout != None and type(timeout) == int: tcpServer.settimeout(timeout)
                self._readyServer = True
            except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError) as err:
                self._readyServer = False
                tcpServer.close()
                sleep(Sock.RECONNECTION_TIMER)
        return tcpServer
    
    def _main_tcp_server(self):
        funcName = '_main_tcp_server'

        while self._runServer:
            if not self._readyServer:
                mainServer = self._open_tcp_server()
                sleep(1)
                continue
            
            try:
                client, address = mainServer.accept()
            except Exception as err:
                sleep(Sock.RECONNECTION_TIMER)
                continue
        
            port = address[1]
            
            # 
            
                
class UdpServer():
    def __init__(self,name:str, ip:str, port:int):
        self.name = name
        self.ip = ip
        self.port = port
        
class Mqtt():
    def __init(self):
        pass