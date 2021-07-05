# -*- coding:utf-8 -*-

# UDP接收消息

from socket import socket,AF_INET,SOCK_DGRAM

# 创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

# 绑定地址/端口号
addr = ("172.16.2.33", 10000)
udpSocket.bind(addr)

# 等待接收对方发送的消息
recvData = udpSocket.recvfrom(1024) # 1024表示本次接收的最大字节数
print(recvData)

# 关闭套接字
udpSocket.close()