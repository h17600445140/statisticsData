
# Socket：（编程接口API）对 TCP/IP 的封装

# Socket之间的连接过程分为三个步骤：服务器监听、客户端请求、连接确认

    import socket
    socket.socket(AddressFamily, Type)
        - AddressFamily: AF_INET(用于Internet进程间通信) AF_UNIX(用于同一台机器进程间通信)
        - Type：SOCK_STREAM(流式套接字，主要用于TCP协议) SOCK_DGRAM(数据报套接字，主要用于UDP协议)
        
# UDP - User Data Protocol, 用户数据报协议
    
    特点：（用于 广播、QQ、视频）
        - 无连接的简单的面向数据报的传输层协议
        - UDP 不提供可靠性
        - 传输速度快
    
 # TCP - Transmission Control Protocol, 传输控制协议
 
     特点：
        - 面向连接的协议
        - 可靠的连接（3次握手、4次挥手）
        - 传输速度慢