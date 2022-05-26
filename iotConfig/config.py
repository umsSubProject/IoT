class ADDRESS:
    SERVER_ADDRESS = '192.168.1.1'
    SYSTEM_ADDRESS = {'(192.168.1.1,8000)':'WEB', '(192.168.1.255,30001)':'SQL'}
    DEVICE_ADDRESS = {'(192.168.1.10,10000)':'MOTION', '(192.168.1.20,10001)':'BUTTON', '(192.168.1.100,20000)':'LIGHT'}

class MqttConfig:
    BROKER_HOST = '127.0.0.1'

    LOCATION = {'192.168.1':'house/admin'}

    SERVER_TOPIC = '#'
    SENSOR_TOPIC = 'sensor/#'
    LIGHT_TOPIC = 'light/#'
    BUTTON_TOPIC = 'button/#'

class ModuleState:
    # 0.initialize
    INPUT_STATE = True
    MONITOR_STATE = True

    # 1.network
    NETWORK_STATE = True

    # 2.web
    WEB_STATE = True