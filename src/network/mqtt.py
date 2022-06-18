import paho.mqtt.client as mqtt
from iotConfig.Classes import MqttData

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