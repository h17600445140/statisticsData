# -*- coding:utf-8 -*-

# tcp 客户端

import socket

# 创建socket
tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
address = ("192.168.1.100", 9999)
tcpClient.connect(address)

# 发送消息
tcpClient.send(" Python ! ".encode('UTF-8'))

# 接受消息
recvData = tcpClient.recv(2024)
print(recvData)

# 关闭套接字
tcpClient.close()
