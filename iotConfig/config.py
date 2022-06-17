class ADDRESS:
    SERVER_ADDRESS = '192.168.1.1'
    SYSTEM_ADDRESS = {'(192.168.1.1,8000)':'WEB', '(192.168.1.255,30001)':'SQL'}
    DEVICE_ADDRESS = {'(192.168.1.10,10000)':'MOTION', '(192.168.1.20,10001)':'BUTTON', '(192.168.1.100,20000)':'LIGHT'}

class MqttConfig:
    BROKER_HOST = '127.0.0.1'
    
    LOCATION = 'house/admin'

    LOCATION = {'192.168.1':'LOCATION'}

    SERVER_TOPIC = '#'
    SENSOR_TOPIC = 'sensor/#'
    LIGHT_TOPIC = 'light/#'
    BUTTON_TOPIC = 'button/#'
    STATE_TOPIC = 'state/#'

class Module:
    # 0.initialize
    INPUT_STATE = 1
    INPUT_STR = 'input'

    # 1.network
    NETWORK_STATE = 0
    NETWORK_STR = 'network'

    # 2.web
    WEB_STATE = 0
    WEB_STR = 'web'
    
    # 3.monitor
    MONITOR_STATE = 0
    MONITOR_STR = 'monitor'
    
    STATE = {
        INPUT_STR : INPUT_STATE, 
        NETWORK_STR : MONITOR_STATE, 
        WEB_STR : NETWORK_STATE, 
        MONITOR_STR : WEB_STATE,
        }
    
    
    
class MainMessege:
    DEVICE_STR = 'device'
    MODULE_STR = 'module'
    
    CMD = {
        DEVICE_STR :1,
        MODULE_STR : Module,
    }