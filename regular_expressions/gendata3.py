# python3

from random import randrange, choice
from string import ascii_lowercase as lc
from time import ctime

tlds = ('com', 'edu', 'net', 'org', 'gov')
maxsize = 2 ** 32   # python3 中sys.maxsize的值过大，通过ctime转换会报错

for i in range(randrange(5, 11)):
    dtsize = randrange(maxsize)
    dtstr = ctime(dtsize)
    llen = randrange(4, 8)
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)
    dom = ''.join(choice(lc) for j in range(dlen))
    print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom, choice(tlds), dtsize,
        llen, dlen))

