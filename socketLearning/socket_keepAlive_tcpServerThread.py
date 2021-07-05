# -*- coding:utf-8 -*-

# tcp 服务器,多线程版本

import socket
import threading


def clientProcess(clientSocket):
    while True:
        # 接收消息
        recvData = clientSocket.recv(1024)
        print(recvData)

        # 发送信息
        clientSocket.send('hello friend!'.encode('UTF-8'))

    # 关闭客户端套接字
    clientSocket.close()


# 创建socket
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定本地信息
address = ("172.16.2.33", 9010)
tcpSocket.bind(address)

# 监听（ 5 表示等待连接的队列长度）
tcpSocket.listen(5)

while True:
    # 创建客户端套接字
    clientSocket,clientAddr = tcpSocket.accept()
    print('接收到客户端的地址为：%s'%clientAddr[0])

    clientThread = threading.Thread(target=clientProcess, args=(clientSocket,))
    clientThread.start()

# 关闭监听套接字
tcpSocket.close()