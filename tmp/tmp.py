from os import path
import sys
sys.path.insert(0,path.abspath('.'))
from iotConfig.config import ADDRESS

a = ADDRESS.SERVER_ADDRESS
print(a)
ADDRESS.SERVER_ADDRESS = 12
print(f'{ADDRESS.SERVER_ADDRESS = }')