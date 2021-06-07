# -*- coding:utf-8 -*-

# fork 不能在windows上面使用

# fork
#   功能：创建进程
#   特点：执行一次，返回两次。子进程永远返回0，父进程返回子进程的pid

import os

pid = os.fork()

if pid < 0:
    print('fork调用失败')
elif pid == 0:
    print('我是子进程：{}'.format(os.getpid()))
    print('我是父进程：{}'.format(os.getppid()))
else:
    print('我是父进程：{}'.format(os.getppid()))
    print('我是子进程：{}'.format(os.getpid()))

print('父子进程都可以执行这里的代码')

