# -*- coding:utf-8 -*-

# tcp 服务器

import socket

# 创建socket
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定本地信息
address = ("172.16.2.33", 9010)
tcpSocket.bind(address)

# 监听（ 5 表示等待连接的队列长度）
tcpSocket.listen(5)

# 创建客户端套接字
newSocket,clientAddr = tcpSocket.accept()
print(clientAddr)

# 接收消息
recvData = newSocket.recv(1024)
print(recvData)

# 发送信息
newSocket.send('hello world!'.encode('UTF-8'))

# 关闭客户端套接字
newSocket.close()

# 关闭监听套接字
tcpSocket.close()