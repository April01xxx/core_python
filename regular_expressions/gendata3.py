# python3

from random import randrange, choice
from string import ascii_lowercase as lc
from time import ctime

file = open('redata.txt', 'w')

tlds = ('com', 'edu', 'net', 'org', 'gov')
maxsize = 2 ** 32   # python3 中sys.maxsize的值过大，通过ctime转换会报错

for i in range(randrange(5, 11)):
    dtsize = randrange(maxsize)
    dtstr = ctime(dtsize)
    llen = randrange(4, 8)
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)
    dom = ''.join(choice(lc) for j in range(dlen))
    # 将内容写入文件而不是屏幕
    #print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom, choice(tlds), dtsize,
    #    llen, dlen))
    file.write('%s::%s@%s.%s::%d-%d-%d\n' % (dtstr, login, dom, choice(tlds),
         dtsize, llen, dlen))

file.close()


import re
with open('redata.txt', 'r') as f:
    for line in f:
        # 时间戳
        date = r'\w{3}\s+\d{1,2}\s\d{2}:\d{2}:\d{2} \d{4}'
        print('Timestamp:', re.search(date, line).group())

        # 电子邮件
        email = r'\w+@\w+\.\w+'
        print('Email:', re.search(email, line).group())

        # 月份
        month = r'(\w{3})\s+\d{1,2}\s\d{2}:\d{2}:\d{2} \d{4}'
        print('Month:', re.search(month, line).group(1))

        # 时间
        tm = r'(\w{3})\s+\d{1,2}\s(\d{2}:\d{2}:\d{2}) \d{4}'
        print('Time:', re.search(tm, line).group(2))

        # 提取月、日、年，然后以“月，日，年”的形式显示
        fmt = r'(\w{3})\s+(\d{1,2})\s\d{2}:\d{2}:\d{2}\s(\d{4})'
        s = re.search(fmt, line)
        if s:
            print('Replace: {},{},{}'.format(s.group(1), s.group(2), s.group(3)))

