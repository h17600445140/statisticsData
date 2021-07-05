# -*- coding:utf-8 -*-

# tcp 客户端

import socket

# 创建socket
tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
address = ("172.16.2.33", 9010)
tcpClient.connect(address)

while True:
    msg = input('请输入将要传送的信息：')

    # 发送消息
    tcpClient.send(msg.encode('UTF-8'))

    # 接受消息
    recvData = tcpClient.recv(2024)
    print(recvData)

    if msg=='bye':
        break

# 关闭套接字
tcpClient.close()