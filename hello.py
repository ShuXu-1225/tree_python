# -*- coding:utf-8 -*-

# ins = input('请输入【1+2+3】的结果 --> ')
# print('1+2+3 = ', ins, 1 + 2 + 3 == int(ins))


# 汉诺塔算法:
# def mov(x, y):
#     print('%s --> %s' % (x, y))
#
#
# def hanoi(n, a, b, c):
#     if n == 1:
#         mov(a, c)
#     else:
#         hanoi(n - 1, a, c, b) #a柱的n-1个盘移到b（借助c）
#         mov(a, c) #a柱的第n个盘移到c
#         hanoi(n - 1, b, a, c) #b柱的n-1个盘移到c（借助a）
#
#
# hanoi(3, 'A', 'B', 'C')


# 使用切片模拟trim操作:
# def trim(s):
#     if s[:1] == ' ':
#         return trim(s[1:len(s)])
#     elif s[-1:] == ' ':
#         return trim(s[:len(s) - 1])
#     else:
#         return s
#
#
# print(trim("   ABC     "))


# 判断是否为可迭代对象:
# from collections import Iterable
#
# print(isinstance('abc', Iterable))  # str是否可迭代


# 将list转换索引-元素:
# for i, value in enumerate(['a', 'b', 'A', 'B']):
#     print(i, ' --> ', value)


# def findMinAndMax(L):
#     min = None
#     max = None
#
#     for i in L:
#         if min == None:
#             min = i
#         elif i < min:
#             min = i
#         if max == None:
#             max = i
#         if i >= max:
#             max = i
#
#     return (min, max)
#
#
# print(findMinAndMax([8, 4, 7, 9, 2]))


# 列出当前目录下全部文件和目录:
# import os
#
# print([d for d in os.listdir('C:\\')])


# 转小写:
# L = ['Hello', 'Python']
# print([s.lower() for s in L])


# LL = ['a', 'b', 'c']
# for i, value in enumerate(LL):
#     print(str(i) + '<-->' + value)


# 杨辉三角 生成器实现:
# def triangles(n):
#     L = [1]
#
#     # print(L)
#     yield L
#
#     it = 1
#     while it < n:
#         it = it + 1
#
#         L = [L[i] + L[i + 1] for i, value in enumerate(L) if i < len(L) - 1]
#
#         L.insert(0, 1)
#         L.append(1)
#
#         # print(L)
#         yield L
#     return L
#
#
# for t in triangles(10):
#     nbsp = ''
#     nbsp += ' ' * int(10 - len(t))
#
#     print(nbsp + str(t))


# from functools import reduce
#
#
# def prod(L):
#     return(reduce(multi, L))
#
#
# def multi(x, y):
#     return x * y
#
#
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#
#
# def byName(t):
#     return t[0]
#
#
# def byScoree(t):
#     return t[1]
#
#
# print(sorted(L, key=byScoree, reverse=True))
# print(sorted(L, key=lambda x:x[1], reverse=False))


# def createCounter():
#     i = 0
#
#     def counter():
#         nonlocal i
#         i = i + 1
#         return i
#
#     return counter


# def createCounter():
#     i = [0]
#
#     def count():
#         i[0] += 1
#         return i[0]
#
#     return count
#
#
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA())


# a = abs
# print(a)
# print(a.__name__)


# 装饰器 decorator:
# import time
#
#
# def metric(func):
#     def wrapper(*args, **kw):
#         start = time.time()
#         d1 = int(round(time.time(), 1000))  # 毫秒级时间
#         func(*args, **kw)
#         end = time.time()
#         d2 = int(round(time.time(), 1000))  # 毫秒级时间
#
#         print('%s executed in %s ms' % (func.__name__, end - start))
#         print('%s executed in %s ms' % (func.__name__, d2 - d1))
#
#     return wrapper
#
#
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y
#
#
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z
#
#
# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')

# 修改类属性:
# class Student(object):
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#
#         self.setCount()
#
#     def setCount(self):
#         Student.count = Student.count + 1
#
#
# a = Student('A')
# b = Student('B')
#
# print(Student.count)


# @property 装饰器:
# class Screen(object):
#     @property
#     def width(self):
#         return self._width
#
#     @property
#     def height(self):
#         return self._height
#
#     @width.setter
#     def width(self, value):
#         self._width = value
#
#     @height.setter
#     def height(self, value):
#         self._height = value
#
#     @property
#     def resolution(self):
#         return self._width * self._height
#
#
# # 测试:
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')


# 定制类 __getattr__:
# class Chain(object):
#
#     def __init__(self, path=''):
#         self._path = path
#
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))
#
#     def __str__(self):
#         return self._path
#
#     __repr__ = __str__
#
#
# Chain().status.user.timeline.list


# 枚举类:
# from enum import Enum
#
# Mon = Enum('Month', ('Jan', 'Fen', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#
# for name, member in Mon.__members__.items():
#     print(name, ' ==> ', member, ' , ', member.value)

# print(int(float('10')))


# 单元测试:
# import unittest
#
#
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def get_grade(self):
#         if self.score >= 60 and self.score < 80:
#             return 'B'
#         if self.score >= 80 and self.score <= 100:
#             return 'A'
#         if self.score < 0 or self.score > 100:
#             raise ValueError
#         return 'C'
#
#
# class TestStudent(unittest.TestCase):
#
#     def setUp(self):
#         print('setUp')
#
#     def tearDown(self):
#         print('tearDown')
#
#     def test_80_to_100(self):
#         s1 = Student('Bart', 80)
#         s2 = Student('Lisa', 100)
#         self.assertEqual(s1.get_grade(), 'A')
#         self.assertEqual(s2.get_grade(), 'A')
#
#     def test_60_to_80(self):
#         s1 = Student('Bart', 60)
#         s2 = Student('Lisa', 79)
#         self.assertEqual(s1.get_grade(), 'B')
#         self.assertEqual(s2.get_grade(), 'B')
#
#     def test_0_to_60(self):
#         s1 = Student('Bart', 0)
#         s2 = Student('Lisa', 59)
#         self.assertEqual(s1.get_grade(), 'C')
#         self.assertEqual(s2.get_grade(), 'C')
#
#     def test_invalid(self):
#         # pass
#
#         s1 = Student('Bart', -1)
#         s2 = Student('Lisa', 101)
#         with self.assertRaises(ValueError):
#             s1.get_grade()
#         with self.assertRaises(ValueError):
#             s2.get_grade()
#
#
# if __name__ == '__main__':
#     unittest.main()


# 文档测试:
# class docTest(object):
#     '''
#
#     a doc test
#
#     >>> d = docTest(10, 10)
#     >>> d.getA()
#     10
#
#     >>> d.getB()
#     30
#
#     '''
#
#     def __init__(self, a, b):
#         self._a = a
#         self._b = b
#
#     def getA(self):
#         return self._a - 10
#
#     def getB(self):
#         return self._b + 10
#
#
# if __name__ == '__main__':
#     import doctest
#
#     doctest.testmod()


# from io import StringIO
#
# f = StringIO('Hello\nHi\nGood')
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())


# from io import BytesIO
# f = BytesIO()
# f.write('徐庶'.encode('utf-8'))
# print(f.getvalue())
#
# ff = BytesIO(b'\xe5\xbe\x90\xe5\xba\xb6')
# print(ff.read())


# import os
#
# # print(os.path.abspath('.'))
# # print(os.listdir('.'))
# #
# # print([x for x in os.listdir('.') if os.path.isdir(x)])
# # print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
#
# print(os.path.abspath('.'))
# print(os.path.split(os.path.abspath('.'))[0])
# print(os.listdir(os.path.split(os.path.abspath('.'))[0]))

# only work in mac and linux:
# import os
#
# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


# from multiprocessing import Process
# import os
#
# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#
#     p = Process(target=run_proc, args=('test',))
#
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')

# from multiprocessing import Pool
# import os, time, random
#
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

# import subprocess
#
# # print('$ nslookup www.python.org')
# # r = subprocess.call(['nslookup', 'www.python.org'])
# # print('Exit code:', r)
#
# rr = subprocess.call(['cmd'])

# import subprocess
#
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# # print(output.decode('utf-8'))
# print(output)
# print('Exit code:', p.returncode)


# from multiprocessing import Process, Queue
# import os, time, random
#
#
# # 写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
#
# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
#
# if __name__ == '__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()


# import time, threading
#
#
# # 新线程执行的代码:
# def loop():
#     print('threadB %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(5)
#     print('threadB %s ended.' % threading.current_thread().name)
#
#
# print('threadA %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('threadA %s ended.' % threading.current_thread().name)


# import threading
#
# # 创建全局ThreadLocal对象:
# local_school = threading.local()
#
#
# def process_student():
#     # 获取当前线程关联的student:
#     std = local_school.student
#     print('Hello, %s (in %s)' % (std, threading.current_thread().name))
#
#
# def process_thread(name):
#     # 绑定ThreadLocal的student:
#     local_school.student = name
#     process_student()
#
#
# t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# import re
#
# reg = re.compile(r'^(\w+)$')
# reg2 = re.compile(r'^([0-9a-zA-Z_]+)$')
# reg3 = re.compile(r'^([_]+)$')
# reg4 = re.compile(r'([@]+)')
# res = reg4.match('@_@')
# print(res.group(0))

# print(re.split(r'@', '1@_@3'))

# import re
#
#
# def name_of_email(addr):
#     reg = re.compile(r'((<([\w\s]+)>)?\s*\w+)@(\w+).(\w+)')
#     res = reg.match(addr)
#     if '<' in res.group(1):
#         return res.group(3)
#     else:
#         return res.group(1)
#
#
# # 测试:
# assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
# assert name_of_email('tom@voyager.org') == 'tom'
# print('ok')


# 时间转换:
# import re
# from datetime import datetime, timezone, timedelta
#
#
# def to_timestamp(dt_str, tz_str):
#     tz_str = re.match(r'UTC\+?(-?[0-9]{1,2}):', tz_str)  # 获取时区
#     tz = timezone(timedelta(hours=int(tz_str.group(1))))  # 创建时区
#     dt_datetime = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')  # str 转 datetime
#     dt_datetime_transed = dt_datetime.replace(tzinfo=tz)  # 强制设置时区
#     tr = dt_datetime_transed.timestamp()  # datetime 转 timestamp
#
#     print(tz)
#     print(dt_datetime)
#     print(dt_datetime_transed)
#     print(tr)
#
#
# t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')


# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key:

# from collections import OrderedDict
#
#
# class LastUpdatedOrderedDict(OrderedDict):
#
#     def __init__(self, capacity):
#         super(LastUpdatedOrderedDict, self).__init__()
#         self._capacity = capacity
#
#     def __setitem__(self, key, value):
#         containsKey = 1 if key in self else 0
#         if len(self) - containsKey >= self._capacity:
#             last = self.popitem(last=False)
#             print('remove:', last)
#         if containsKey:
#             del self[key]
#             print('set:', (key, value))
#         else:
#             print('add:', (key, value))
#         OrderedDict.__setitem__(self, key, value)
#
#
# orderedDict = LastUpdatedOrderedDict(3)
# orderedDict.__setitem__('a', 1)
# orderedDict.__setitem__('b', 2)
# orderedDict.__setitem__('c', 3)
# orderedDict.__setitem__('b', 9)
# orderedDict.__setitem__('a', 9)
# orderedDict.__setitem__('d', 9)
#
# print(orderedDict)

# s1 = b'hello'
# s2 = '您好'
#
# print(s1)
# print(s2)
#
# print(type(s1))
# print(type(s2))
#
# print(s2.encode(encoding='utf-8'))
#
# print(b'\xe6\x82\xa8\xe5\xa5\xbd'.decode(encoding='utf-8'))


# 公式计算圆周率:
# import itertools
#
#
# def pi(N):
#     ' 计算pi的值 '
#     # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
#     it = itertools.count(1, 2)
#     # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
#     ns = itertools.takewhile(lambda x: x <= 2 * N - 1, it)
#     # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
#     nss = [4 / (pow(-1, i) * value) for i, value in enumerate(ns)]
#     # step 4: 求和:
#     nsum = sum(nss)
#
#     return nsum
#
#
# print(pi(10000000))

# 使用closing实现上下文管理:
# from contextlib import closing
# from urllib.request import urlopen
#
# with closing(urlopen('http://www.baidu.com')) as page:
#     for line in page:
#         print(line)

# from urllib import request
#
# with request.urlopen('http://www.baidu.com') as f:
#     data = f.read()
#     print('Status --> ', f.status, f.reason)
#
#     for k, v in f.getheaders():
#         print('%s : %s' % (k, v))
#
#     print('Data --> ', data.decode('utf-8'))

# from urllib import request
#
# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent',
#                'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))

# from urllib import request, parse
#
# print('Login to weibo.cn...')
# email = input('Email: ')
# passwd = input('Password: ')
# login_data = parse.urlencode([
#     ('username', email),
#     ('password', passwd),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])
#
# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent',
#                'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer',
#                'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
#
# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))


# from urllib import request
#
#
# def fetch_data(url):
#     with request.urlopen(url) as f:
#         dd = f.read()
#         # dd = data.decode('utf-8')
#         print(type(dd))
#         # return data.decode(encode='utf-8')
#
#         import json
#         print(type(json.loads(dd)))
#
#         return(json.loads(dd))
#
#
# # 测试
# URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
# data = fetch_data(URL)
# print(data)
# assert data['query']['results']['channel']['location']['city'] == 'Beijing'
# print('ok')

# 解析XML:

# from xml.parsers.expat import ParserCreate
#
#
# class DefaultSaxHandler(object):
#     def start_element(self, name, attrs):
#         print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
#
#     def end_element(self, name):
#         print('sax:end_element: %s' % name)
#
#     def char_data(self, text):
#         print('sax:char_data: %s' % text)
#
#
# xml = r'''<?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''
#
# handler = DefaultSaxHandler()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(xml)


# 解析xml格式天气:
# from xml.parsers.expat import ParserCreate
# from urllib import request
#
#
# class WeatherHandler(object):
#     forecastDic = {}
#     arry = list()
#
#     def start_element(self, name, attrs):
#         if name == 'yweather:location':
#             # print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
#             self.forecastDic['city'] = attrs['city']
#         elif name == 'yweather:forecast':
#             itemInfo = {}
#             for key, v in attrs.items():
#                 itemInfo[key] = v
#             self.arry.append(itemInfo)
#
#     def end_element(self, name):
#         if name == 'yweather:location':
#             print('sax:end_element: %s' % name)
#             if name == 'channel':
#                 self.forecastDic['forecast'] = self.arry
#
#     def char_data(self, text):
#         # print('sax:char_data: %s' % text)
#         pass
#
#
# def parseXml(xml_str):
#     handler = WeatherHandler()
#     parser = ParserCreate()
#     parser.StartElementHandler = handler.start_element
#     parser.EndElementHandler = handler.end_element
#     parser.CharacterDataHandler = handler.char_data
#     parser.Parse(xml_str)
#     print(handler.forecastDic)
#     print(handler.arry)
#
#
# URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'
#
# with request.urlopen(URL, timeout=4) as f:
#     data = f.read()
#
# result = parseXml(data.decode('utf-8'))
# # assert result['city'] == 'Beijing'


# 读取网页，并解析html:

# from urllib import request
# from html.parser import HTMLParser
#
#
# class MyHtmlParser(HTMLParser):
#     __type = ''
#
#     def __init__(self):
#         HTMLParser.__init__(self)
#         self.__list_recent_events = False
#
#     def handle_starttag(self, tag, attrs):
#         def _attr(attrlist, attrname):
#             for attr in attrlist:
#                 if attr[0] == attrname:
#                     return attr[1]
#             return None
#
#         #  class list-recent-events
#         if tag == 'ul' and _attr(attrs, 'class').find('list-recent-events') != -1:
#             self.__list_recent_events = True
#
#         # print(1)
#         # print('<%s>' % tag)
#         # if ('class', 'event-title') in attrs:
#         #     MyHtmlParser.__type = 'name'  # 设置爬取名称状态
#         # if tag == 'time':
#         #     MyHtmlParser.__type = 'time'
#         # if ('class', 'say-no-more') in attrs:
#         #     MyHtmlParser.__type = 'year'
#         # if ('class', 'event-location') in attrs:
#         #     MyHtmlParser.__type = 'location'
#         # pass
#
#     def handle_endtag(self, tag):
#         # print(2)
#         # print('</%s>' % tag)
#         if tag == 'ul':
#             print('--------->')
#         pass
#
#     # def handle_startendtag(self, tag, attrs):
#     #     print('<%s/>' % tag)
#
#     def handle_data(self, data):
#         # print(3)
#         if self.__list_recent_events and self.lasttag == 'a':
#             print('<a> --> ', data)
#
#     # def handle_comment(self, data):
#     #     print('<!--', data, '-->')
#
#     # def handle_entityref(self, name):
#     #     print('&%s;' % name)
#     #
#     # def handle_charref(self, name):
#     #     print('&#%s;' % name)
#
#
# with request.urlopen("https://www.python.org/events/python-events/") as page:
#     f = page.read()
#     # print(f.decode('utf-8'))
#
#     parser = MyHtmlParser()
#     parser.feed(f.decode('utf-8'))
#     parser.feed('''
#     <p><p>abc</p></p>
#     ''')

# from html.parser import HTMLParser
# from urllib import request
# import sys, io
#
#
# class MyHTMLParser(HTMLParser):
#     # __init__()方法意义重大的原因有两个。
#     # 第一个原因是在对象生命周期中初始化是最重要的一步；每个对象必须正确初始化后才能正常工作。
#     # 第二个原因是__init__()参数值可以有多种形式。
#
#     def __init__(self):
#         # 利用父类构造函数
#         HTMLParser.__init__(self)
#         # list，即将开展的活动
#         self.upcoming = []
#         # list，错过的活动
#         self.missed = []
#         # 每一个会议的数据
#         self.item = []
#         # 是否错过的标志
#         self.ismiss = False
#         # tuple,我们关心的信息
#         self.flag = {
#             'h3': False,
#             'time': False,
#             'span': False
#         }
#
#     def handle_starttag(self, tag, attrs):
#         # 按网页元素顺序判断，这样可以减少判断次数
#         # 通过starttag来判断这一行是不是我们想要获取的信息以及是我们想获取的哪一类信息。将相关属性，例如self.flag['h3']，置为True.然后在handle_data中通过判断这些相关属性的值，来知道我们要不要记录这些值和这些值要归属在哪个相关属性上。
#         # 如果标签是h3,并且属性class的值是‘widget-title just-missed’，就将相关属性置为True
#         if tag == 'h3' and self._attr(attrs, 'class') == 'widget-title just-missed':
#             self.ismiss = True
#         if tag == 'h3' and self._attr(attrs, 'class') == 'event-title':
#             self.flag['h3'] = True
#         if tag == 'time':
#             self.flag['time'] = True
#         if tag == 'span' and self._attr(attrs, 'class') == 'event-location':
#             self.flag['span'] = True
#
#     def handle_data(self, data):
#         # 利用完相关信息后，还要将相关属性恢复为默认值，以便解析下一行
#         if self.flag['h3']:
#             self.item.append(data)
#             self.flag['h3'] = False
#         if self.flag['time']:
#             self.item.append(data)
#             self.flag['time'] = False
#         if self.flag['span']:
#             self.item.append(data)
#             if not self.ismiss:
#                 self.upcoming.append(self.item)
#             else:
#                 self.missed.append(self.item)
#             self.flag['span'] = False
#             # 当遍历到span元素时，说明为一轮，到下一轮时要重置
#             self.item = []
#
#     # 这个方法用来获取我们想要的attrname的值。无论这一行有多少attr,调用这个函数_attr(attrs,attrname),都可以获取到我们想要的属性的值
#     def _attr(self, attrlist, attrname):
#         for attr in attrlist:
#             if attr[0] == attrname:
#                 return attr[1]
#         return None
#
#
# def getHtml():
#     sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码
#     with request.urlopen('https://www.python.org/events/python-events/') as f:
#         data = f.read().decode('utf-8')
#     return data
#
#
# parser = MyHTMLParser()
# # parser.feed(getHtml())
# # 可以写个函数进行纯数据改造
# # print(parser.upcoming, parser.missed)
#
# parser.feed('''
# <h3 class="event-title"><a href="/events/python-events/733/">PyCon Nigeria</a></h3><h3 class="event-title"><a href="/events/python-events/733/">1</a></h3><h3 class="event-title">2</h3>
# ''')

# pillow:

# from PIL import Image, ImageFilter
#
# im = Image.open('F:/backgrounds/134795680831.jpg')
# w, h = im.size
# print(w, '-', h)
# im.thumbnail((w // 3, h // 3))
# im2 = im.filter(ImageFilter.BLUR)
#
# im2.show()
#
# # im.save('test.jpg', 'jpeg')


# 图形验证码:
# from PIL import Image, ImageDraw, ImageFont, ImageFilter
#
# import random
#
#
# # 随机字母:
# def rndChar():
#     return chr(random.randint(65, 90))
#
#
# # 随机颜色1:
# def rndColor():
#     return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
#
#
# # 随机颜色2:
# def rndColor2():
#     return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
#
#
# # 240 x 60:
# width = 60 * 4
# height = 60
# image = Image.new('RGB', (width, height), (255, 255, 255))
# # 创建Font对象:
# font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
# # 创建Draw对象:
# draw = ImageDraw.Draw(image)
# # 填充每个像素:
# for x in range(width):
#     for y in range(height):
#         draw.point((x, y), fill=rndColor())
# # 输出文字:
# for t in range(4):
#     draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# # 模糊:
# # image = image.filter(ImageFilter.BLUR)
# # image.save('code.jpg', 'jpeg')
#
# image.show()


# from PIL import Image, ImageDraw, ImageFont, ImageFilter
#
# import random
#
#
# # Random char, rotate, background color, font color, posation
# def rndChar():
#     return chr(random.randint(65, 90))
#
#
# def rndRotate():
#     return random.randint(-75, 75)
#
#
# def rndBgColor():
#     # return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
#     return (random.randint(32, 255), random.randint(32, 255), random.randint(32, 255))
#
#
# def rndFontColor():
#     # return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
#     return (random.randint(0, 120), random.randint(0, 120), random.randint(0, 120))
#
#
# def rndPosation(i):
#     return (60 * i + random.randint(0, 15), random.randint(-10, 10))
#
#
# # clear
# def fillImg(width, height, img):
#     for x in range(width):
#         for y in range(height):
#             img.point((x, y), fill=rndBgColor())
#
#
# def addNewChar(image):
#     # Init
#     char = Image.new('RGB', fontSize, defaultColor)
#     drawChar = ImageDraw.Draw(char)
#
#     # Random
#     rChar = rndChar()
#     rotate = rndRotate()
#     posation = rndPosation(i)
#
#     # Draw and rotate
#     drawChar.text((10, 10), rChar, fill=rndFontColor(), font=font)
#     char = char.rotate(rotate)
#
#     # Split
#     r, g, b = char.split()
#
#     # Paste
#     image.paste(char, posation, r)
#     image.paste(char, posation, g)
#     image.paste(char, posation, b)
#
#
# # Canvas Size : 240 x 60 ,Font Size = 60 x 60, Default Color = #000000
# imageSize = (240, 60)
# fontSize = (60, 60)
# defaultColor = (0, 0, 0)
#
# # New Image
# image = Image.new('RGB', imageSize, defaultColor)
# font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
# drawImage = ImageDraw.Draw(image)
# fillImg(imageSize[0], imageSize[1], drawImage)
#
# # Blur background
# image = image.filter(ImageFilter.BLUR)
#
# # Add Char
# for i in range(4):
#     addNewChar(image)
#
# # Blur all
# # image = image.filter(ImageFilter.BLUR)
#
# # Save
# # image.save('code.jpg', 'jpeg')
# image.show()


# requests:

import requests

# # r = requests.get('http://www.baidu.com')
# # print(r.status_code)
# # print(r.text)
# #
# rr = requests.get('http://www.baidu.com', params={'a': 1, 'b': 2})
# # print(rr.url)
# # print(rr.encoding)
# # print(rr.content)
# print(rr.cookies['BDORZ'])
#
# rrr = requests.get(
#     'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# # print(rrr.json())
# print(rrr.cookies)

# import requests
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
# res = requests.get('http://hu.58.com', headers=headers)
# print(res.text)


# psutil:
# import psutil

# print(psutil.cpu_count())
# for x in range(10):
#     print(psutil.cpu_percent(interval=1, percpu=True))
# print(psutil.swap_memory())
# print(psutil.disk_partitions())
# print(psutil.disk_usage('F:\\'))
# print(psutil.disk_io_counters())
# print(psutil.net_io_counters())
# print(psutil.net_if_addrs())
# print(psutil.net_if_stats())
# print(psutil.net_connections())
# print(psutil.pids())
# p = psutil.Process(11792)
# print(p.name())
# print(p.exe())
# print(p.cpu_times())
# psutil.test()


# from tkinter import *
# import tkinter.messagebox as messagebox
#
#
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidget()
#
#     def createWidget(self):
#         # self.helloLabel = Label(self, text='Hello text')
#         # self.helloLabel.pack()
#         # self.quitButton = Button(self, text='quit this', command=self.quit)
#         # self.quitButton.pack()
#
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.subButton = Button(self, text='sub', command=self.sayHello)
#         self.subButton.pack()
#
#     def sayHello(self):
#         name = self.nameInput.get() or 'ABC'
#         messagebox.showinfo('Message', 'Hello %s' % name)
#
#
# app = Application()
# app.master.title('ABC')
# app.mainloop()

# import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('www.w3school.com.cn', 80))
#
# s.send(b'GET / HTTP/1.1\r\nHost: www.w3school.com.cn\r\nConnection: close\r\n\r\n')
#
# buffer = []
# while True:
#     d = s.recv(1024)  # 每次最多接收1k字节:
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
#
# s.close()
#
# header, html = data.split(b'\r\n\r\n', 1)
#
# print(header.decode('utf-8'))
#
# with open('sina.html', 'wb') as f:  # 把接收的数据写入文件:
#     f.write(html)

# print(socket.gethostname())

# 邮件 发送:
# from email.mime.text import MIMEText
# from email.header import Header
# from email.utils import parseaddr, formataddr
#
#
# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))
#
#
# from_addr = 'xushu_fighting@163.com'
# from_pwd = 'xushu@198912'
# to_addr = 'jinghongzhixian@126.com'
# smtp_server = 'smtp.163.com'
# smtp_port = 25
#
# msg = MIMEText('Hello from pathon', 'plain', 'utf-8')  # plain表示文本
# msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
# msg['To'] = _format_addr('管理员 <%s>' % to_addr)
# msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
#
# import smtplib
#
# server = smtplib.SMTP(smtp_server, smtp_port)
# server.set_debuglevel(1)
# server.login(from_addr, from_pwd)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

# # 邮件 获取:
# import poplib
# from email.parser import Parser
#
# mail_name = 'xushu_fighting@163.com'
# mail_pwd = 'xushu@198912'
# pop_server = 'pop.163.com'
#
# server = poplib.POP3(pop_server)
# server.set_debuglevel(1)
# print(server.getwelcome().decode('utf-8'))
#
# server.user(mail_name)
# server.pass_(mail_pwd)
#
# print('Message : %s, Size : %s' % server.stat())
#
# # print(server.list())
# resp, mails, octets = server.list()
#
# index = len(mails)  # the newest mail`s id
#
# # print(server.retr(index))
# resq, lines, octets = server.retr(index)
#
# msg_content = b'\r\n'.join(lines).decode('utf-8')
# msg = Parser().parsestr(msg_content)
#
# # server.dele(index) # 删除服务器上的邮件
#
# server.quit()
#
# # 解析邮件:
# # msg可能是嵌套的MIMEMultipart
# # 递归打印 indent用于缩进
# from email.header import decode_header
# from email.utils import parseaddr
#
#
# def decode_str(s):
#     value, charset = decode_header(s)[0]
#     if charset:
#         value = value.decode(charset)
#     return value
#
#
# def guess_charset(msg):
#     charset = msg.get_charset()
#     if charset is None:
#         content_type = msg.get('Content-type', '').lower()
#         pos = content_type.find('charset=')
#         if pos >= 0:
#             charset = content_type[pos + 8:].strip()
#     return charset
#
#
# def print_info(msg, indent=0):
#     if indent == 0:
#         for header in ['From', 'To', 'Subject']:
#             value = msg.get('header', '')
#             if value:
#                 if header == 'Subject':
#                     value = decode_str(value)
#                 else:
#                     hdr, addr = parseaddr(value)
#                     name = decode_str(hdr)
#                     value = u'%s<%s>' % (name, addr)
#             print('%s%s: %s' % ('  ' * indent, header, value))
#     if (msg.is_multipart()):
#         parts = msg.get_payload()
#         for n, part in enumerate(parts):
#             print('%spart %s' % ('  ' * indent, n))
#             print('%s--------------------' % ('  ' * indent))
#             print_info(part, indent + 1)
#     else:
#         content_type = msg.get_content_type()
#         if (content_type == 'text/plain' or content_type == 'text/html'):
#             content = msg.get_payload(decode=True)
#             charset = guess_charset(msg)
#             if charset:
#                 content = content.decode(charset)
#             print('%sText: %s' % ('  ' * indent, content + '...'))
#         else:
#             print('%sAttachment: %s' % ('  ' * indent, content_type))
#
#
# print_info(msg)


# # 数据库 sqlite:
# # -*- coding: utf-8 -*-
#
# import os, sqlite3
#
# db_file = os.path.join(os.path.dirname(__file__), 'test.db')
# if os.path.isfile(db_file):
#     os.remove(db_file)
#
# # 初始数据:
# conn = sqlite3.connect(db_file)
# cursor = conn.cursor()
# cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
# cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
# cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
# cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
# cursor.close()
# conn.commit()
# conn.close()
#
#
# def get_score_in(low, high):
#     ' 返回指定分数区间的名字，按分数从低到高排序 '
#     connin = sqlite3.connect('test.db')
#     cursorin = connin.cursor()
#     cursorin.execute('select name from user as a where a.score > ? and a.score <= ? order by score ', (low, high))
#     # print('cursorin.rowcount', cursorin.rowcount) # insert update delete
#     value = cursorin.fetchall()
#     cursorin.close()
#     connin.close()
#
#     value = list(map(lambda x: x[0], value))
#     return value
#
#     # result = list()
#     # if len(value) > 0:
#     #     for item in value:
#     #         result.append(item[0])
#     #
#     # return result
#
#
# # 测试:
# assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
# assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
# assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)
#
# print('Pass')

# # 数据库 mysql:
# import mysql.connector
#
# conn = mysql.connector.connect(user='root', password='tiger', database='mysql')
# # cursor = conn.cursor()
# # cursor.execute('create table test (id varchar(20) primary key, name varchar(20))')
# # cursor.execute('insert into test (id, name) values (%s, %s)', ['1', 'C'])
# # cursor.execute('insert into test (id, name) values (%s, %s)', ['2', 'A'])
# # cursor.execute('insert into test (id, name) values (%s, %s)', ['3', 'B'])
# # print(cursor.rowcount)
# # conn.commit()  # 提交事务
# # cursor.close()
#
# cursor = conn.cursor()
# cursor.execute('select * from test where id > %s', (1,))
# values = cursor.fetchall()
# print(values)
# cursor.close()
# conn.close()

# # sqlalchemy ORM:
# from sqlalchemy import Column, String, create_engine, ForeignKey
# from sqlalchemy.orm import sessionmaker, relationship
# from sqlalchemy.ext.declarative import declarative_base
#
# Base = declarative_base()  # 对象的基类
#
#
# class Test1(Base):
#     __tablename__ = 'test1'
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#
#     child = relationship('Test2')  # 一对多
#
#
# class Test2(Base):
#     __tablename__ = 'test2'
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#
#     user_id = Column(String(20), ForeignKey('test1.id'))  # test2 通过外键 test1.id 映射到 test1
#
#
# engine = create_engine('mysql+mysqlconnector://root:tiger@localhost:3306/mysql')
# DBSession = sessionmaker(bind=engine)
#
# session = DBSession()
#
# session.execute('drop table if exists test1')
# session.execute('drop table if exists test2')
#
# session.execute('create table test1 (id varchar(20) primary key, name varchar(20))')
# session.execute(
#     'create table test2 (id varchar(20) primary key, name varchar(20), user_id varchar(20) references test1(id))')
#
# new_test1 = Test1(id='7', name='7A')
# new_test2 = Test1(id='8', name='8A')
# new_test3 = Test1(id='9', name='9A')
# new_testt1 = Test2(id='88', name='88A', user_id='8')
# new_testt2 = Test2(id='99', name='99A', user_id='9')
# session.add(new_test1)
# session.add(new_test2)
# session.add(new_test3)
# session.add(new_testt1)
# session.add(new_testt2)
#
# session.commit()
# session.close()
#
# session = DBSession()
# res = session.query(Test1).filter(Test1.id == '8').one()
# print(res.name, ' ----> ', res.child[0].name)
# session.close()

# # 协程:
# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         print('[Consumer] consume %s' % n)
#         r = '200 ok'
#
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[Produce] product %s' % n)
#         r = c.send(n)
#         print('[Consumer return %s]' % r)
#     c.close()
#
#
# c = consumer()
# produce(c)

# # asyncio 1:
# import asyncio
#
#
# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(5)
#     print("Hello again!")
#
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()

# # asyncio2:
# import threading
# import asyncio
#
#
# @asyncio.coroutine
# def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(3)
#     print('Hello again! (%s)' % threading.currentThread())
#
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# # asyncio3:
# import asyncio
#
#
# @asyncio.coroutine
# def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     # Ignore the body, close the socket
#     writer.close()
#
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# aiohttp:
import asyncio

from aiohttp import web


async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>', content_type='text/html')


async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'), content_type='text/html')


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
