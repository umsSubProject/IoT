import socket
import logging
import time
from threading import Thread
from multiprocessing import Queue, Process
from ctypes import windll
from pi.connect import Mqtt

from src.mcu.mcu import *
from src.sql.sql import *
from src.web.web import *
from iotConfig.config import ModuleState

timeBeginPeriod = windll.winmm.timeBeginPeriod
timeBeginPeriod(1,)

class IoT():
    def __init__(self):
        self.name = 'IoT_main'

        self.inputThread = Thread(target = self.input_module)
        self.monitorThread = Thread(target = self.monitor_module)
        self.networkThread = Thread(target = self.network_module)
        self.webThread = Thread(target = self.web_module)
        
        self.mqtt = None
        self.web = None
        self.Monitor = None

    def input_module(self):
        while 1:
            input_msg = input('Please enter a command : ').strip()
            if not input_msg: continue
            try:
                id, cmd = input_msg.split()
                if id in ModuleState.INIT_STATE:
                    ModuleState.INIT_STATE[id] = cmd
            except Exception as err:
                print('input error')
                print(f'{err = }')

    def network_module(self):
        if not self.mqtt:
            self.mqtt = Mqtt()
        self.mqtt.run()

    def web_module(self):
        pass

    def monitor_module(self):
        pass

    def run(self):
        inputState = ModuleState.INIT_STATE['INPUT_STATE']
        monitorState = ModuleState.INIT_STATE['MONITOR_STATE']
        networkState = ModuleState.INIT_STATE['NETWORK_STATE']
        webState = ModuleState.INIT_STATE['WEB_STATE']

        while 1:
            # 0.command
            if inputState and not self.inputThread.is_alive():
                try:
                    inputState = False
                    self.inputThread.start()
                except Exception as err:
                    inputState = ModuleState.INIT_STATE['INPUT_STATE']
                    print(err)


            # 1.network
            if networkState and not self.inputThread.is_alive():
                try:
                    networkState = False
                    self.networkThread.start()
                except Exception as err:
                    networkState = ModuleState.INIT_STATE['NETWORK_STATE']
                    print(err)

            # 2.web
            if webState and not not self.webThread.is_alive():
                try:
                    webState = False
                    self.webThread.start()
                except Exception as err:
                    webState = ModuleState.INIT_STATE['WEB_STATE']
                    print(err)

            # 3.monitor
            if monitorState and not self.inputThread.is_alive():
                try:
                    monitorState = False
                    self.monitorThread.start()
                except Exception as err:
                    monitorState = ModuleState.INIT_STATE['MONITOR_STATE']
                    print(err)
        
        

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