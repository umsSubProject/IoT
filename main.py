import socket
import logging
import time
import ctypes
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

        self.inputThread = Thread()
        self.monitorThread = Thread()
        self.networkThread = Thread()
        self.webThread = Thread()
        
        # self._inputState = ModuleState.INIT_STATE[ModuleState.INPUT_STR]
        # self._monitorState = ModuleState.INIT_STATE[ModuleState.MONITOR_STR]
        # self._networkState = ModuleState.INIT_STATE[ModuleState.NETWORK_STR]
        # self._webState = ModuleState.INIT_STATE[ModuleState.WEB_STR]

        self._threadState = ModuleState.INIT_STATE
        
        self.mqtt = Mqtt()
        self.web = None
        self.Monitor = None

    def input_module(self):
        funcName = 'MODULE_INPUT'
        while self._threadState[ModuleState.INPUT_STR]:
            input_msg = input('Please enter a command : ').strip().split()
            if not input_msg or len(input_msg)<2:
                print(f'No information found. Please enter it again.')
                continue
            try:
                header, cmd_bool = input_msg[0].lower(), int(input_msg[1])
                if header in ModuleState.INIT_STATE:
                    self._threadState[header] = cmd_bool
            except Exception as err:
                print(f'Error {funcName} : {err}')
                print(f'No information found. Please enter it again.')
        else:
            print(f'To fail to input module... {ModuleState.INPUT_STR = }')
            print('Exit Program...')

    def network_module(self):
        self.mqtt.run()

    def web_module(self):
        funcName = 'MODULE_WEB'
        while self._threadState[ModuleState.WEB_STR]:
            continue

    def monitor_module(self):
        funcName = 'MODULE_MONITOR'
        while self._threadState[ModuleState.MONITOR_STR]:
            continue
    
    def _raise_exception(self, id, name = 'none'):
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(id, ctypes.py_object(SystemExit))
        
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(id,0)
            print(f'Exception raise failure name:{name}({id})')

    def run(self):
        funcName = 'RUN'

        while 1:
            # 0.command
            if self._threadState[ModuleState.INPUT_STR] and not self.inputThread.is_alive():
                try:
                    self.inputThread = Thread(target = self.input_module, name = 'INPUT')
                    self.inputThread.start()
                except Exception as err:
                    print(f'Error {funcName} : {err}')

            # 1.network
            if self._threadState[ModuleState.NETWORK_STR] and not self.networkThread.is_alive():
                try:
                    self.networkThread = Thread(target = self.network_module, name = 'NETWORK', daemon = True)
                    self.networkThread.start()
                except Exception as err:
                    print(f'Error {funcName} : {err}')

            # 2.web
            if self._threadState[ModuleState.WEB_STR] and not not self.webThread.is_alive():
                try:
                    self.webThread = Thread(target = self.web_module, name = 'WEB', daemon = True)
                    self.webThread.start()
                except Exception as err:
                    print(f'Error {funcName} : {err}')

            # 3.monitor
            if self._threadState[ModuleState.MONITOR_STR] and not self.monitorThread.is_alive():
                try:
                    self.monitorThread = Thread(target = self.monitor_module, name = 'MONITOR', daemon = True)
                    self.monitorThread.start()
                except Exception as err:
                    print(f'Error {funcName} : {err}')
        
        

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