import socket
from time import sleep

class UdpServer():
    def __init__(self,name:str, ip:str, port:int):
        self.name = name
        self.ip = ip
        self.port = port
        
