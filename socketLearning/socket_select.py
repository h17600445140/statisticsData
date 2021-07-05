# -*- coding:utf-8 -*-

# select 多路复用

import select
import socket
import sys


# 创建socket
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定本地信息
address = ("192.168.1.100", 9999)
tcpSocket.bind(address)

# 监听（ 5 表示等待连接的队列长度）
tcpSocket.listen(5)

# ----------
inputs = [tcpSocket, sys.stdin]
# ----------

running = True

while True:

    # 调用select函数，阻塞等待
    readable,writeable,exceptional = select.select(inputs, [], [])

    # 数据抵达、循环
    for sock in readable:
        # 监听到有新的连接
        if sock == tcpSocket:
            connect,address = tcpSocket.accept()
            # select 监听的socket
            inputs.append(connect)
        elif sock == sys.stdin:
            cmd = sys.stdin.readline()
            running = False
            break
        # 有数据到达
        else:
            # 读取客户端连接发送的数据
            data = sock.recv(1024)
            if data:
                print(data)
                sock.send(data)
            else:
                # 移除select监听的socket
                sock.close()
                inputs.remove(sock)

        # 如果监听到有用户数据敲击键盘，那么就退出
        if not running:
            break

tcpSocket.close()




















