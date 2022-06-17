from iotConfig.config import ModuleState

b = {
    '1':1,
    '2':2,
    '3':3
}
a = {
    'a':b,
    'd':[1,2,3,4]
}
nn = a['a']['1']
print(nn)
# nnn = nn['b']
# print(nnn)