# -*- coding:utf-8 -*-

# ECHO回环

from socket import socket,AF_INET,SOCK_DGRAM

# 创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

# 绑定地址/端口号
addr = ("172.16.2.33", 10000)
udpSocket.bind(addr)

num = 1

# 等待接收对方发送的消息
while True:
    # 1024表示本次接收的最大字节数
    recvData = udpSocket.recvfrom(1024)
    print(recvData)
    # 将接受到的消息发送给对方
    udpSocket.sendto(recvData[0], recvData[1])

    if num == 10:
        break
    num += 1

# 关闭套接字
udpSocket.close()