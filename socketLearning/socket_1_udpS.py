# -*- coding:utf-8 -*-

# UDP发送消息

from socket import socket,AF_INET,SOCK_DGRAM

# 创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

# 准备接收方的地址
sendAddr = ("172.16.2.33", 10000)

# 从键盘获取发送数据
data = input('请输入要发送的数据：')
sendData = data.encode('UTF-8')

# 发送数据到指定电脑上去
udpSocket.sendto(sendData, sendAddr)

# recvData = udpSocket.recvfrom(1024)
# print(recvData)

# 关闭套接字
udpSocket.close()