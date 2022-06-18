def test():
    print('a')

b = {'a':test}

c = 'a'
if c in b:
    print('c')
    print(b[c])