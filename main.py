import socket, logging, time
from threading import Thread
from multiprocessing import Queue, Process
from ctypes import windll

from src.mcu.mcu import *
from src.sql.sql import *
from src.web.web import *

timeBeginPeriod = windll.winmm.timeBeginPeriod
timeBeginPeriod(1,)

class IoT():
    def __init__(self):
        self.name = None


    def run():
        pass

if __name__ == '__main__':
    syncTime = int(time.time())

    mcuQueue = Queue()
    webQueue = Queue()
    sqlQueue = Queue()
    
    #  To be scheduled
    # appQueue = Queue()
    
    mcuProcess = Process(target = run_mcu_process, name = 'MCU_Process', daemon=True, args = (mcuQueue, syncTime,))
    webProcess = Process(target = run_web_process, name = 'WEB_Process', daemon=True, args = (webQueue, syncTime,))
    sqlProcess = Process(target = run_sql_process, name = 'SQL_Process', daemon=True, args = (sqlQueue, syncTime,))
    
    main = IoT()
    main.run()