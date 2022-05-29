import socket
from time import sleep
import paho.mqtt.client as mqtt

from iotConfig.Classes import MqttData
from iotConfig.parameter import Sock

class TcpServer():
    def __init__(self,name:str, ip:str, port:int):
        self.name = name
        self.ip = ip
        self.port = port

        self._runServer = True
        self._readyServer = False

    def get_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
            print(f'not ')
        finally:
            s.close()
        return IP

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
    """
    Topic -> Location/Sensor_Type/Subject
    ex) house/room/switch/light
    """
    def __init__(self, ip, queue):
        self.mqttC = mqtt.Client()
        self.queue_msg = queue
        self.mqttC.on_connect = self.on_connect
        self.mqttC.on_disconnect = self.on_disconnect
        self.mqttC.on_reconnect = self.on_reconnect
        self.mqttC.on_message = self.on_message
        self.ip = ip
        
        self.mqtt = MqttData()
        #

    def on_connect(self, client, userdata, flag, rc):
        print(f'Connected with result code {rc}')

    def on_message(self):
        pass
    
    def subscribe(self):
        pass

    def publish(self):
        pass

    def run(self):
        try:
            # connect Broker
            self.mqttC.connect()

            # loop msg
            self.mqttC.loop_forever()
        except Exception as err:
            print(f'{err = }')
        except KeyboardInterrupt:
            print('raise interreption')

def process_mqtt(queue_msg, syncTime):
    networkMQTT = Mqtt(queue_msg, syncTime)
    networkMQTT.run()