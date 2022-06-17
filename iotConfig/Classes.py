from time import time


class Message():
    def __init__(self):
        self.name = ''
        self.status = 0
        self.lastUpdate = time()
        self.updateCnt = 0
        self.updateRate = 0
        
    def get_stat(self):
        return {'name': self.name,
                'status': self.status,
                'lastUpdate': self.lastUpdate,
                'updateCount': self.updateCnt,
                'updateRate': self.updateRate}
        
    def get_stat_string(self):
        return f'{self.name},{self.status},{self.lastUpdate},{self.updateCnt},{self.updateRate}'


class MqttData(Message):
    NAME = 'MQTTDATA'
    
    def __init__(self):
        super().__init__()
        self.name = MqttData.NAME
        self.isAliva, self.status = 0, 0
        
        self.topic = ''
        self.msg = ''

    def set_data_from_string(self, data: str):
        funcName = 'set_data_from_string'
        

class ConvertType():
    str_to_num = {}
    name_to_str = {}
    
class Device():
    def __init__(self, name = ''):
        self.name = name
        self.status = 0