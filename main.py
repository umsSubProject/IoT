import socket, logging, time
from threading import Thread
from multiprocessing import Queue, Process
from ctypes import windll

from src.mcu.mcu import *
from src.sql.sql import *
from src.web.web import *
from config.config import ModuleState

timeBeginPeriod = windll.winmm.timeBeginPeriod
timeBeginPeriod(1,)

class IoT():
    def __init__(self):
        self.name = None

    def input_module(self):
        pass

    def network_module(self):
        pass

    def run():
        inputState = ModuleState.INPUT_STATE
        networkState = ModuleState.NETWORK_STATE

        while 1:
            # 0.input
            if inputState:
                inputState = False
                input_module = Thread(target = input_module, deamon = True)
                input_module.start()

            # 1.network
            if networkState:
                networkState = False
                network_module = Thread(target = network_module, deamon = True)
                network_module.start()

            # 2.video

            # 3.web
        
        pass

if __name__ == '__main__':
    syncTime = int(time.time())

    mcuQueue = Queue()
    webQueue = Queue()
    sqlQueue = Queue()
    
    #  To be scheduled
    # appQueue = Queue()
    
    webProcess = Process(target = run_web_process, name = 'WEB_Process', daemon=True, args = (webQueue, syncTime,))
    sqlProcess = Process(target = run_sql_process, name = 'SQL_Process', daemon=True, args = (sqlQueue, syncTime,))
    
    main = IoT()
    main.run()