import socket
import logging
import time
from threading import Thread
from multiprocessing import Queue, Process
from ctypes import windll

from src.mcu.mcu import *
from src.sql.sql import *
from src.web.web import *
from iotConfig.config import ModuleState

timeBeginPeriod = windll.winmm.timeBeginPeriod
timeBeginPeriod(1,)

class IoT():
    def __init__(self):
        self.name = None

        self.inputThread = Thread(target = self.input_module)
        self.monitorThread = Thread(target = self.monitor_module)
        self.networkThread = Thread(target = self.network_module)
        self.webThread = Thread(target = self.web_module)

    def input_module(self):
        pass

    def monitor_module(self):
        pass

    def network_module(self):
        pass

    def web_module(self):
        pass

    def run(self):
        inputState = ModuleState.INPUT_STATE
        monitorState = ModuleState.MONITOR_STATE
        networkState = ModuleState.NETWORK_STATE
        webState = ModuleState.WEB_STATE

        while 1:
            # 0.initialize
            if inputState and not self.inputThread.is_alive():
                try:
                    inputState = False
                    self.inputThread.start()
                except Exception as err:
                    print(err)
            
            if monitorState and not self.inputThread.is_alive():
                try:
                    monitorState = False
                    self.monitorThread.start()
                except Exception as err:
                    print(err)


            # 1.network
            if networkState and not self.inputThread.is_alive():
                try:
                    networkState = False
                    self.networkThread.start()
                except Exception as err:
                    print(err)

            # 2.web
            if webState and not not self.webThread.is_alive():
                try:
                    webState = False
                    self.webThread.start()
                except Exception as err:
                    print(err)

            # 3.video
        
        

if __name__ == '__main__':
    syncTime = int(time.time())

    mcuQueue = Queue()
    webQueue = Queue()
    sqlQueue = Queue()
    
    #  To be scheduled
    # appQueue = Queue()
    
    # webProcess = Process(target = run_web_process, name = 'WEB_Process', daemon=True, args = (webQueue, syncTime,))
    # sqlProcess = Process(target = run_sql_process, name = 'SQL_Process', daemon=True, args = (sqlQueue, syncTime,))
    
    main = IoT()
    main.run()